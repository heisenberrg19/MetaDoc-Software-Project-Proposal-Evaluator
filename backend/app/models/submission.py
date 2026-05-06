"""
Submission and SubmissionToken models
"""

from datetime import datetime
import pytz
from sqlalchemy import Text
from app.core.extensions import db
from app.models.base import BaseModel, SubmissionStatus


class Submission(BaseModel):
    """Submission model - Core entity for document submissions"""
    __tablename__ = 'submissions'
    
    # Submission metadata
    job_id = db.Column(db.String(36), unique=True, nullable=False, index=True)
    file_name = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.BigInteger, nullable=False)
    file_hash = db.Column(db.String(64), nullable=False)
    mime_type = db.Column(db.String(100), nullable=False)
    file_modified_at = db.Column(db.DateTime, nullable=True)
    file_content = db.deferred(db.Column(db.LargeBinary, nullable=True))
    
    # Submission details
    submission_type = db.Column(db.String(50), nullable=False)
    google_drive_link = db.Column(db.String(500), nullable=True)
    student_id = db.Column(db.String(50), nullable=True)
    student_name = db.Column(db.String(255), nullable=True)
    semester = db.Column(db.String(10), nullable=True)
    submitted_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Processing status
    status = db.Column(db.Enum(SubmissionStatus), default=SubmissionStatus.PENDING, nullable=False)
    processing_started_at = db.Column(db.DateTime, nullable=True)
    processing_completed_at = db.Column(db.DateTime, nullable=True)
    error_message = db.Column(Text, nullable=True)
    
    # Foreign keys
    professor_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    deadline_id = db.Column(db.String(36), db.ForeignKey('deadlines.id', ondelete='CASCADE'), nullable=True)
    
    # Relationships
    analysis_result = db.relationship('AnalysisResult', backref='submission', uselist=False, lazy=True)
    audit_logs = db.relationship('AuditLog', backref='submission', lazy=True)
    
    @property
    def is_late(self):
        """Check if submission was made after the deadline"""
        return self.get_days_late() > 0

    def get_days_late(self):
        """
        Calculate how many days late the submission is.
        Returns 0 if on time or no deadline.
        Returns fractional days (e.g. 1.2) if late.
        """
        try:
            if not self.deadline_id:
                return 0
            from app.models.deadline import Deadline
            deadline = Deadline.query.filter_by(id=self.deadline_id).first()
            if not deadline:
                return 0
                
            # Use the later of created_at (submission time) or file_modified_at (last edit time)
            # This is essential for GDrive links to catch edits made after the deadline.
            submission_time = self.created_at
            if self.file_modified_at and self.file_modified_at > submission_time:
                submission_time = self.file_modified_at
                
            created_at_utc = submission_time.replace(tzinfo=pytz.UTC)
            deadline_dt = deadline.deadline_datetime
            
            if deadline.timezone and deadline.timezone != 'UTC':
                try:
                    local_tz = pytz.timezone(deadline.timezone)
                    deadline_aware = local_tz.localize(deadline_dt)
                    deadline_utc = deadline_aware.astimezone(pytz.UTC)
                except Exception:
                    deadline_utc = deadline_dt.replace(tzinfo=pytz.UTC)
            else:
                deadline_utc = deadline_dt.replace(tzinfo=pytz.UTC)
            
            if created_at_utc <= deadline_utc:
                return 0
                
            diff = created_at_utc - deadline_utc
            return diff.total_seconds() / 86400.0
        except Exception:
            return 0
    
    @property
    def last_modified(self):
        """Return the last modification time"""
        return self.updated_at if self.updated_at else self.created_at
    
    @property
    def analysis_summary(self):
        """Return a summary of the analysis results"""
        if not self.analysis_result:
            return None
            
        # Safely handle potential stringified JSON
        stats = self.analysis_result.content_statistics
        if isinstance(stats, str):
            import json
            try:
                stats = json.loads(stats)
            except:
                stats = {}
        elif not stats:
            stats = {}
            
        return {
            'word_count': stats.get('word_count') if isinstance(stats, dict) else None,
            'readability_score': self.analysis_result.flesch_kincaid_score,
            'is_complete': self.analysis_result.is_complete_document
        }
    
    def __repr__(self):
        return f'<Submission {self.job_id}>'
    
    def to_dict(self):
        created_at_iso = self.created_at.isoformat()
        if not created_at_iso.endswith('Z') and '+' not in created_at_iso:
            created_at_iso += 'Z'
            
        last_modified_iso = self.last_modified.isoformat() if self.last_modified else None
        if last_modified_iso and not last_modified_iso.endswith('Z') and '+' not in last_modified_iso:
            last_modified_iso += 'Z'

        started_at_iso = self.processing_started_at.isoformat() if self.processing_started_at else None
        if started_at_iso and not started_at_iso.endswith('Z') and '+' not in started_at_iso:
            started_at_iso += 'Z'

        completed_at_iso = self.processing_completed_at.isoformat() if self.processing_completed_at else None
        if completed_at_iso and not completed_at_iso.endswith('Z') and '+' not in completed_at_iso:
            completed_at_iso += 'Z'

        return {
            'id': self.id,
            'job_id': self.job_id,
            'file_name': self.file_name,
            'original_filename': self.original_filename,
            'file_size': self.file_size,
            'mime_type': self.mime_type,
            'submission_type': self.submission_type,
            'student_id': self.student_id,
            'student_name': self.student_name,
            'semester': self.semester,
            'status': self.status.value,
            'is_late': self.is_late,
            'last_modified': last_modified_iso,
            'analysis_summary': self.analysis_summary,
            'created_at': created_at_iso,
            'processing_started_at': started_at_iso,
            'processing_completed_at': completed_at_iso,
            'error_message': self.error_message
        }


class SubmissionToken(BaseModel):
    """Submission Token model for student access"""
    __tablename__ = 'submission_tokens'
    
    token = db.Column(db.String(255), unique=True, nullable=False, index=True)
    professor_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    usage_count = db.Column(db.Integer, default=0)
    max_usage = db.Column(db.Integer, nullable=True)
    deadline_id = db.Column(db.String(36), db.ForeignKey('deadlines.id', ondelete='SET NULL'), nullable=True)
    
    professor = db.relationship('User', backref='submission_tokens')
    deadline = db.relationship('Deadline', backref='submission_tokens')
    
    def __repr__(self):
        return f'<SubmissionToken {self.token[:8]}... by {self.professor_id}>'
    
    def is_valid(self):
        """Check if token is still valid"""
        if not self.is_active:
            return False
        if self.expires_at < datetime.utcnow():
            return False
        if self.max_usage and self.usage_count >= self.max_usage:
            return False
        return True
