# Routing Documentation

## Overview
The IPFS Control Panel uses React Router DOM for client-side routing, providing seamless navigation between different pages without full page reloads.

## How It Works

### 1. Router Setup
The application wraps all routes in a `BrowserRouter` component in `App.jsx`:
```jsx
<Router>
  <Routes>
    <Route path="/" element={<Dashboard />} />
    <Route path="/phishing-cids" element={<PhishingCIDs />} />
    // ... more routes
  </Routes>
</Router>
```

### 2. Route Structure
- **Dashboard**: `/` - Main overview page with statistics and charts
- **Phishing CIDs**: `/phishing-cids` - CID management and analysis
- **Campaigns**: `/campaigns` - Campaign management interface
- **Gateways**: `/gateways` - Gateway monitoring and management
- **System Health**: `/system-health` - Service uptime monitoring

### 3. Navigation Component
The `Navigation.jsx` component uses `Link` components for navigation:
```jsx
<Link to={item.path} className="nav-item">
  {item.label}
</Link>
```

### 4. Active State Detection
Routes automatically highlight the active page using `useLocation()` hook to detect current pathname and apply active styling.

### 5. Protected Routes
All routes are wrapped in `ProtectedRoute` component, ensuring users must be authenticated before accessing any page.
