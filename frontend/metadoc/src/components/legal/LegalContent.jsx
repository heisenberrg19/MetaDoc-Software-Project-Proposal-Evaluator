const LEGAL_CONTENT = {
  privacy: {
    title: 'Privacy Policy',
    intro:
      'This policy explains what information MetaDoc collects, how it is used, and how it is protected when you sign in with Google and use the submission or evaluation features.',
    sections: [
      {
        heading: '1. Information we collect',
        paragraphs: [
          'MetaDoc may collect the information you provide directly and the information returned by Google during sign-in.'
        ],
        list: [
          'Google account information such as your name, email address, and profile picture.',
          'User role and account details used to manage professor and student access.',
          'Submission data, including uploaded files, Google Drive links, and document metadata.',
          'Technical information such as session tokens, timestamps, and basic usage logs used for security and troubleshooting.'
        ]
      },
      {
        heading: '2. How we use information',
        list: [
          'Authenticate users through Google Sign-In.',
          'Match student accounts to class-list records.',
          'Access Google Drive files only for submission validation, document analysis, and related workflow functions.',
          'Store evaluation results, reports, and submission records for the academic workflow of the application.',
          'Detect errors, prevent abuse, and maintain service reliability.'
        ]
      },
      {
        heading: '3. Data sharing and storage',
        paragraphs: [
          'MetaDoc does not sell personal data. Data is used only for operating the application and supporting the academic review process.'
        ],
        list: [
          'We may store user and submission records in the application database.',
          'OAuth access tokens are used only to complete Google-related actions requested by the user.',
          'Google Drive data is accessed only as needed for the features you use.',
          'We do not intentionally share your personal data with third parties except where required to run the service or comply with law.'
        ]
      },
      {
        heading: '4. Your choices',
        list: [
          'You may stop using the app at any time.',
          'You can request correction or deletion of your account data by contacting us.',
          'You may remove app permissions from your Google Account settings if applicable.'
        ]
      },
      {
        heading: '5. Contact',
        paragraphs: [
          'If you have questions about this policy or how your information is handled, contact heisenberrg19@gmail.com.'
        ]
      }
    ]
  },
  terms: {
    title: 'Terms of Service',
    intro:
      'These terms explain who may use MetaDoc, how the service may be used, and the responsibilities that apply when you sign in and submit or review academic documents.',
    sections: [
      {
        heading: '1. Eligibility',
        paragraphs: [
          'MetaDoc is intended for students, professors, and authorized reviewers who have permission to use the system. You must use your own account and follow your institution\'s access rules.'
        ]
      },
      {
        heading: '2. Acceptable use',
        list: [
          'Use the app only for legitimate academic document submission, review, and evaluation purposes.',
          'Do not upload malicious, illegal, offensive, or unauthorized files.',
          'Do not attempt to bypass authentication, access other users\' data, or disrupt the service.',
          'Do not use the app in a way that violates your school policies or Google\'s terms.'
        ]
      },
      {
        heading: '3. User responsibilities',
        list: [
          'You are responsible for the accuracy of the information and files you submit.',
          'If you share a submission link, make sure you are authorized to do so.',
          'You are responsible for maintaining the security of your Google account and session.',
          'Student users should only use the submission portal for the class and deadline they were invited to join.'
        ]
      },
      {
        heading: '4. Service and content',
        list: [
          'MetaDoc may analyze documents, store evaluation results, and generate reports based on the data available.',
          'Analysis results are provided to support academic review and should not be treated as a final legal or institutional decision.',
          'We may modify, suspend, or discontinue parts of the service when needed for maintenance, security, or updates.'
        ]
      },
      {
        heading: '5. Limitation and contact',
        paragraphs: [
          'MetaDoc is provided as an academic project and is offered as-is. If you have questions about these terms, contact heisenberrg19@gmail.com.'
        ]
      }
    ]
  }
};

const LegalContent = ({ type = 'privacy' }) => {
  const legalData = LEGAL_CONTENT[type] || LEGAL_CONTENT.privacy;

  return (
    <div className="legal-modal-body-content">
      <p className="legal-modal-intro">{legalData.intro}</p>
      {legalData.sections.map((section) => (
        <section key={section.heading} className="legal-modal-section">
          <h3>{section.heading}</h3>
          {section.paragraphs?.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
          {section.list?.length ? (
            <ul>
              {section.list.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          ) : null}
        </section>
      ))}
    </div>
  );
};

export const getLegalTitle = (type) => (LEGAL_CONTENT[type]?.title || LEGAL_CONTENT.privacy.title);

export default LegalContent;
