import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { useState } from 'react'
import { AuthProvider } from './contexts/AuthContextProvider'
import ProtectedRoute from './components/ProtectedRoute'
import Header from './components/Header'
import Navigation from './components/Navigation'
import Dashboard from './pages/Dashboard'
import PhishingCIDs from './pages/PhishingCIDs'
import Campaigns from './pages/Campaigns'
import Gateways from './pages/Gateways'
import SystemHealth from './pages/SystemHealth'

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const handleMenuToggle = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <AuthProvider>
      <Router>
        <ProtectedRoute>
          <div className="min-h-screen bg-gray-50 flex">
            <Navigation isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />
            <div className="flex-1 flex flex-col lg:ml-0">
              <Header onMenuToggle={handleMenuToggle} />
              <main className="flex-1">
                <Routes>
                  <Route path="/" element={<Dashboard />} />
                  <Route path="/phishing-cids" element={<PhishingCIDs />} />
                  <Route path="/campaigns" element={<Campaigns />} />
                  <Route path="/gateways" element={<Gateways />} />
                  <Route path="/system-health" element={<SystemHealth />} />
                </Routes>
              </main>
            </div>
          </div>
        </ProtectedRoute>
      </Router>
    </AuthProvider>
  );
}

export default App
