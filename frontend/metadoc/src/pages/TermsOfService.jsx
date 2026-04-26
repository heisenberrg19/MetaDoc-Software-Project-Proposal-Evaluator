import LegalContent from '../components/legal/LegalContent';
import { useNavigate } from 'react-router-dom';
import { ChevronLeft } from '../components/common/Icons';
import Button from '../components/common/Button/Button';
import '../styles/Login.css';

const TermsOfService = () => {
  const navigate = useNavigate();

  return (
    <div className="submission-theme" style={{ minHeight: '100vh', padding: '2rem' }}>
      <div className="legal-page-container" style={{ maxWidth: '800px', margin: '0 auto', background: 'white', padding: '3rem', borderRadius: '24px', boxShadow: 'var(--shadow-xl)' }}>
        <div style={{ marginBottom: '2rem' }}>
          <Button 
            variant="outline" 
            onClick={() => navigate(-1)}
            icon={() => <ChevronLeft size={20} />}
          >
            Back
          </Button>
        </div>
        <h1 className="premium-card-title" style={{ textAlign: 'left', fontSize: '2.5rem', marginBottom: '1.5rem' }}>Terms of Service</h1>
        <div className="legal-content-wrapper">
          <LegalContent type="terms" />
        </div>
        <div style={{ marginTop: '3rem', paddingTop: '2rem', borderTop: '1px solid #eee', color: '#666', fontSize: '0.9rem' }}>
          <p>© 2025 MetaDoc • Cebu Institute of Technology - University</p>
        </div>
      </div>
    </div>
  );
};

export default TermsOfService;
