import React from 'react';

function ElectionTimeline({ election }) {
  return (
    <section className="timeline" aria-labelledby="timeline-heading">
      <h2 id="timeline-heading">Election Timeline</h2>
      <div className="timeline-container" role="list">
        {election.steps.map((step, index) => (
          <div 
            key={step.id} 
            className="timeline-item" 
            role="listitem"
            tabIndex="0"
            aria-label={`Step ${index + 1}: ${step.title}`}
          >
            <div className="timeline-marker">{index + 1}</div>
            <div className="timeline-content">
              <h3>{step.title}</h3>
              {step.date && <p className="date" aria-label="Date">{new Date(step.date).toLocaleDateString()}</p>}
              <p className="description">{step.description}</p>
              {step.duration && <p className="duration" aria-label="Duration">{step.duration}</p>}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default ElectionTimeline;
