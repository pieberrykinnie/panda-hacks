import { useState, useEffect } from 'react'
import { User } from '@supabase/supabase-js'
import { supabase } from './lib/supabase'
import { AuthComponent } from './components/Auth'
import './App.css'

/**
 * Main application component with authentication state management
 */
function App() {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Get initial session
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    // Listen for auth changes
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
    })

    return () => subscription.unsubscribe()
  }, [])

  if (loading) {
    return <div>Loading...</div>
  }

  if (!user) {
    return (
      <div className="app">
        <h1>StudyStreak</h1>
        <p>Your personalized, gamified study companion</p>
        <AuthComponent />
      </div>
    )
  }

  return (
    <div className="app">
      <h1>Welcome to StudyStreak!</h1>
      <p>Hello, {user.email}</p>
      <button onClick={() => supabase.auth.signOut()}>
        Sign Out
      </button>
    </div>
  )
}

export default App
