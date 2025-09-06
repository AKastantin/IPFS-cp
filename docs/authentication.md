# Authentication System

## Overview

The IPFS Control Panel uses React Context API for authentication state management. Users must log in to access the dashboard, with sessions persisting for 8 hours.

## File Structure

```
src/
├── contexts/
│   └── AuthContext.jsx      # Central auth state management
├── components/
│   ├── Login.jsx           # Login form component
│   ├── ProtectedRoute.jsx  # Route protection wrapper
│   └── Header.jsx          # Header with logout button
└── App.jsx                 # Main app with auth provider
```

## Authentication Flow

1. **App loads** → `AuthContext` checks localStorage for existing session
2. **No session** → Shows `Login` component
3. **Valid session** → Shows protected content via `ProtectedRoute`
4. **User logs in** → Credentials validated, session stored in localStorage
5. **User logs out** → Session cleared, redirected to login

## AuthContext Structure

```javascript
// src/contexts/AuthContext.jsx
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const login = async (username, password) => { /* ... */ };
  const logout = () => { /* ... */ };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

## Usage

### Login Credentials
- **Username**: `ipfs`
- **Password**: `926Ehkry46LY`

### Using AuthContext
```javascript
import { useAuth } from '../contexts/AuthContext';

function MyComponent() {
  const { isAuthenticated, user, login, logout } = useAuth();
  
  if (!isAuthenticated) return <Login />;
  return <div>Welcome, {user.username}!</div>;
}
```

### Protected Routes
```javascript
<AuthProvider>
  <ProtectedRoute>
    <Dashboard />
  </ProtectedRoute>
</AuthProvider>
```

## Session Management

- **Storage**: Browser localStorage
- **Duration**: 8 hours
- **Keys**: `authToken`, `userData`, `sessionExpiry`
- **Auto-expiry**: Sessions expire automatically

## Security Notes

⚠️ **Demo Only**: This uses hardcoded credentials. For production:
- Implement backend authentication
- Use password hashing
- Add proper session management
- Implement CSRF protection
