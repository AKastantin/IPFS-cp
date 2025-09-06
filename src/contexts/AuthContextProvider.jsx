import { useState, useEffect } from 'react';
import { AuthContext } from './AuthContext';

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    // Check for existing session on app load
    useEffect(() => {
        const checkAuthStatus = () => {
            const token = localStorage.getItem('authToken');
            const userData = localStorage.getItem('userData');
            const sessionExpiry = localStorage.getItem('sessionExpiry');

            if (token && userData && sessionExpiry) {
                const now = new Date().getTime();
                const expiry = parseInt(sessionExpiry);

                if (now < expiry) {
                    // Session is still valid
                    setIsAuthenticated(true);
                    setUser(JSON.parse(userData));
                } else {
                    // Session expired, clear storage
                    clearAuthData();
                }
            }
            setLoading(false);
        };

        checkAuthStatus();
    }, []);

    const clearAuthData = () => {
        localStorage.removeItem('authToken');
        localStorage.removeItem('userData');
        localStorage.removeItem('sessionExpiry');
        setIsAuthenticated(false);
        setUser(null);
    };

    const login = async (username, password) => {
        // Simulate API call with the specified credentials
        if (username === 'ipfs' && password === '926Ehkry46LY') {
            const userData = {
                username: 'ipfs',
                role: 'analyst',
                loginTime: new Date().toISOString()
            };

            // Generate a simple token (in real app, this would come from server)
            const token = btoa(JSON.stringify({ username, timestamp: Date.now() }));

            // Set session expiry to 8 hours from now (as per requirements)
            const sessionExpiry = new Date().getTime() + (80 * 60 * 60 * 1000);

            // Store in localStorage
            localStorage.setItem('authToken', token);
            localStorage.setItem('userData', JSON.stringify(userData));
            localStorage.setItem('sessionExpiry', sessionExpiry.toString());

            setIsAuthenticated(true);
            setUser(userData);

            return { success: true };
        } else {
            return { success: false, error: 'Invalid username or password' };
        }
    };

    const logout = () => {
        clearAuthData();
    };

    const value = {
        isAuthenticated,
        user,
        loading,
        login,
        logout
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};
