import { ReactNode } from 'react'
import { useAuth } from '../hooks/useAuth'
import { AuthComponent } from './Auth'

interface ProtectedRouteProps {
  children: ReactNode
}

/**
 * Protected route component that requires authentication
 * @param children - React components to render when authenticated
 * @returns Auth component if not authenticated, children if authenticated
 */
export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { user, loading } = useAuth()

  if (loading) {
    return (
      <div className="loading-container">
        <div>Loading...</div>
      </div>
    )
  }

  if (!user) {
    return (
      <div className="auth-container">
        <h1>StudyStreak</h1>
        <p>Your personalized, gamified study companion</p>
        <AuthComponent />
      </div>
    )
  }

  return <>{children}</>
}