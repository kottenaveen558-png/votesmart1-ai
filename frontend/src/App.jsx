import React, { useState, useEffect } from 'react';
import ElectionTimeline from './components/ElectionTimeline';
import ProcessSteps from './components/ProcessSteps';

function App() {
  const [elections, setElections] = useState([]);
  const [selectedElection, setSelectedElection] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchElections();
  }, []);

  const fetchElections = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${import.meta.env.VITE_API_URL}/elections`);
      if (!response.ok) throw new Error('Failed to fetch elections');
      const data = await response.json();
      setElections(data);
      if (data.length > 0) {
        setSelectedElection(data[0]);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div role="status" aria-live="polite">Loading...</div>;
  if (error) return <div role="alert">{error}</div>;

  return (
    <div className="app" role="main">
      <header>
        <h1>Election Process Education</h1>
        <p>Learn how elections work, step by step</p>
      </header>
      
      <main>
        <section className="elections-selector">
          <label htmlFor="election-select">Select Election:</label>
          <select 
            id="election-select"
            value={selectedElection?.id || ''} 
            onChange={(e) => setSelectedElection(elections.find(el => el.id === e.target.value))}
            aria-label="Select election to view"
          >
            {elections.map(election => (
              <option key={election.id} value={election.id}>
                {election.name}
              </option>
            ))}
          </select>
        </section>

        {selectedElection && (
          <>
            <ElectionTimeline election={selectedElection} />
            <ProcessSteps election={selectedElection} />
          </>
        )}
      </main>
    </div>
  );
}

export default App;
