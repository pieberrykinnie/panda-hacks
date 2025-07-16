import { useAuth } from '../hooks/useAuth'

/**
 * Dashboard component for authenticated users
 * Displays user profile and main application features
 */
export function Dashboard() {
  const { user, signOut } = useAuth()

  const handleSignOut = async (): Promise<void> => {
    try {
      await signOut()
    } catch (error) {
      console.error('Error signing out:', error)
    }
  }

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>StudyStreak Dashboard</h1>
        <div className="user-info">
          <span>Welcome, {user?.email}</span>
          <button onClick={handleSignOut} className="sign-out-btn">
            Sign Out
          </button>
        </div>
      </header>
      
      <main className="dashboard-content">
        <section className="study-stats">
          <h2>Your Study Stats</h2>
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Current Streak</h3>
              <p className="stat-value">0 days</p>
            </div>
            <div className="stat-card">
              <h3>Longest Streak</h3>
              <p className="stat-value">0 days</p>
            </div>
            <div className="stat-card">
              <h3>Total Study Time</h3>
              <p className="stat-value">0 hours</p>
            </div>
          </div>
        </section>
        
        <section className="quick-actions">
          <h2>Quick Actions</h2>
          <div className="action-buttons">
            <button className="action-btn primary">Create Study Plan</button>
            <button className="action-btn secondary">View Progress</button>
            <button className="action-btn secondary">Join Study Group</button>
          </div>
        </section>
      </main>
    </div>
  )
}