import { ProtectedRoute } from './components/ProtectedRoute'
import { Dashboard } from './components/Dashboard'
import './App.css'

/**
 * Main application component with protected routes
 * Uses authentication state to conditionally render content
 */
function App() {
  return (
    <div className="app">
      <ProtectedRoute>
        <Dashboard />
      </ProtectedRoute>
    </div>
  )
}

export default App
