import { Link, useLocation } from 'react-router-dom';

const Navigation = ({ isOpen, onClose }) => {
    const location = useLocation();

    const navItems = [
        { path: '/', label: 'Dashboard', icon: '📊' },
        { path: '/phishing-cids', label: 'Phishing CIDs', icon: '🛡️' },
        { path: '/campaigns', label: 'Campaigns', icon: '🎯' },
        { path: '/gateways', label: 'Gateways', icon: '🌐' },
        { path: '/system-health', label: 'System Health', icon: '💚' },
    ];

    const isActive = (path) => {
        if (path === '/') {
            return location.pathname === '/';
        }
        return location.pathname.startsWith(path);
    };

    return (
        <>
            {/* Mobile overlay */}
            {isOpen && (
                <div
                    className="fixed inset-0 bg-gray-600 bg-opacity-75 z-20 lg:hidden"
                    onClick={onClose}
                />
            )}

            {/* Sidebar */}
            <div className={`fixed inset-y-0 left-0 z-30 w-64 bg-white shadow-lg transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0 ${isOpen ? 'translate-x-0' : '-translate-x-full'
                }`}>
                {/* Sidebar header */}
                <div className="flex items-center justify-between h-16 px-4 border-b border-gray-200">
                    <div className="flex items-center">
                        <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                            <span className="text-white font-bold text-sm">IPFS</span>
                        </div>
                        <span className="ml-3 text-lg font-semibold text-gray-900">Control Panel</span>
                    </div>
                    <button
                        onClick={onClose}
                        className="lg:hidden p-2 rounded-md text-gray-400 hover:text-gray-600 hover:bg-gray-100"
                    >
                        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                {/* Navigation items */}
                <nav className="mt-8 px-4">
                    <div className="space-y-2">
                        {navItems.map((item) => (
                            <Link
                                key={item.path}
                                to={item.path}
                                onClick={onClose}
                                className={`flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors duration-200 ${isActive(item.path)
                                    ? 'bg-blue-50 text-blue-700 border-r-2 border-blue-700'
                                    : 'text-gray-700 hover:bg-gray-50 hover:text-gray-900'
                                    }`}
                            >
                                <span className="text-lg mr-3">{item.icon}</span>
                                <span>{item.label}</span>
                            </Link>
                        ))}
                    </div>
                </nav>

                {/* Sidebar footer */}
                <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-200">
                    <div className="flex items-center text-sm text-gray-500">
                        <div className="w-2 h-2 bg-green-400 rounded-full mr-2"></div>
                        System Online
                    </div>
                </div>
            </div>
        </>
    );
};

export default Navigation;