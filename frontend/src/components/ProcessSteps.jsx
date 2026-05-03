import React from 'react';

function ProcessSteps({ election }) {
  return (
    <section className="process-steps" aria-labelledby="steps-heading">
      <h2 id="steps-heading">How to Participate</h2>
      <div className="steps-grid" role="list">
        {election.steps.map((step) => (
          <article 
            key={step.id} 
            className="step-card"
            role="listitem"
          >
            <h3>{step.title}</h3>
            <p>{step.description}</p>
            {step.duration && (
              <span className="badge" aria-label="Duration">{step.duration}</span>
            )}
          </article>
        ))}
      </div>
    </section>
  );
}

export default ProcessSteps;
