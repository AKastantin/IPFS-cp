function SystemHealth() {
    // Sample service data - in real app this would come from API
    const services = [
        {
            name: 'CID Notify Service',
            description: 'Handles CID detection notifications and processing',
            port: '9090',
            status: 'up',
            uptime: '99.9%',
            lastCheck: '2 minutes ago',
            responseTime: '45ms'
        },
        {
            name: 'Gateway Server',
            description: 'Manages IPFS gateway connections and monitoring',
            port: '9191',
            status: 'up',
            uptime: '99.7%',
            lastCheck: '1 minute ago',
            responseTime: '120ms'
        },
        {
            name: 'PDNS Processor',
            description: 'Processes PassiveDNS queries and gateway discovery',
            port: '9393',
            status: 'up',
            uptime: '99.8%',
            lastCheck: '30 seconds ago',
            responseTime: '78ms'
        },
        {
            name: 'Control Panel API',
            description: 'REST API for control panel operations',
            port: '6655',
            status: 'up',
            uptime: '100%',
            lastCheck: '15 seconds ago',
            responseTime: '23ms'
        },
        {
            name: 'MongoDB Database',
            description: 'Primary database for storing detection data',
            port: '27017',
            status: 'up',
            uptime: '99.9%',
            lastCheck: '1 minute ago',
            responseTime: '12ms'
        },
        {
            name: 'Redis Cache',
            description: 'Caching layer for improved performance',
            port: '6379',
            status: 'down',
            uptime: '95.2%',
            lastCheck: '5 minutes ago',
            responseTime: 'N/A'
        },
        {
            name: 'Elasticsearch',
            description: 'Search and analytics engine for log data',
            port: '9200',
            status: 'up',
            uptime: '99.5%',
            lastCheck: '2 minutes ago',
            responseTime: '156ms'
        },
        {
            name: 'Prometheus Metrics',
            description: 'Metrics collection and monitoring system',
            port: '9091',
            status: 'up',
            uptime: '99.8%',
            lastCheck: '45 seconds ago',
            responseTime: '34ms'
        }
    ];

    const getStatusColor = (status) => {
        switch (status) {
            case 'up':
                return 'bg-green-100 text-green-800 border-green-200';
            case 'down':
                return 'bg-red-100 text-red-800 border-red-200';
            case 'warning':
                return 'bg-yellow-100 text-yellow-800 border-yellow-200';
            default:
                return 'bg-gray-100 text-gray-800 border-gray-200';
        }
    };

    const getStatusIcon = (status) => {
        switch (status) {
            case 'up':
                return '✅';
            case 'down':
                return '❌';
            case 'warning':
                return '⚠️';
            default:
                return '❓';
        }
    };

    const overallStatus = services.every(service => service.status === 'up') ? 'up' : 'down';
    const upServices = services.filter(service => service.status === 'up').length;
    const totalServices = services.length;

    return (
        <div className="bg-gray-50">
            {/* Main Content */}
            <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                <div className="px-4 py-6 sm:px-0">
                    {/* Page Header */}
                    <div className="mb-8">
                        <h1 className="text-3xl font-bold text-gray-900">System Health</h1>
                        <p className="mt-2 text-gray-600">Monitor service uptimes and system status</p>
                    </div>

                    {/* Overall Status Cards */}
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                        <div className="bg-white overflow-hidden shadow rounded-lg">
                            <div className="p-5">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <div className={`w-8 h-8 rounded-md flex items-center justify-center ${overallStatus === 'up' ? 'bg-green-500' : 'bg-red-500'
                                            }`}>
                                            <span className="text-white font-bold text-sm">
                                                {overallStatus === 'up' ? '✓' : '✗'}
                                            </span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Overall Status</dt>
                                            <dd className={`text-lg font-medium ${overallStatus === 'up' ? 'text-green-600' : 'text-red-600'
                                                }`}>
                                                {overallStatus === 'up' ? 'All Systems Up' : 'Issues Detected'}
                                            </dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-white overflow-hidden shadow rounded-lg">
                            <div className="p-5">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <div className="w-8 h-8 bg-blue-500 rounded-md flex items-center justify-center">
                                            <span className="text-white font-bold text-sm">🔧</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Total Services</dt>
                                            <dd className="text-lg font-medium text-gray-900">{totalServices}</dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-white overflow-hidden shadow rounded-lg">
                            <div className="p-5">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <div className="w-8 h-8 bg-green-500 rounded-md flex items-center justify-center">
                                            <span className="text-white font-bold text-sm">✅</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Services Up</dt>
                                            <dd className="text-lg font-medium text-gray-900">{upServices}</dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-white overflow-hidden shadow rounded-lg">
                            <div className="p-5">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <div className="w-8 h-8 bg-red-500 rounded-md flex items-center justify-center">
                                            <span className="text-white font-bold text-sm">❌</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Services Down</dt>
                                            <dd className="text-lg font-medium text-gray-900">{totalServices - upServices}</dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Service List */}
                    <div className="bg-white shadow rounded-lg overflow-hidden">
                        <div className="px-6 py-4 border-b border-gray-200">
                            <h3 className="text-lg font-medium text-gray-900">Service Status</h3>
                            <p className="text-sm text-gray-500">Real-time monitoring of all system services</p>
                        </div>

                        <div className="overflow-x-auto">
                            <table className="min-w-full divide-y divide-gray-200">
                                <thead className="bg-gray-50">
                                    <tr>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Service
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Description
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Port
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Status
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Uptime
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Response Time
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Last Check
                                        </th>
                                    </tr>
                                </thead>
                                <tbody className="bg-white divide-y divide-gray-200">
                                    {services.map((service, index) => (
                                        <tr key={index} className="hover:bg-gray-50">
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="flex items-center">
                                                    <span className="text-lg mr-3">{getStatusIcon(service.status)}</span>
                                                    <div>
                                                        <div className="text-sm font-medium text-gray-900">
                                                            {service.name}
                                                        </div>
                                                    </div>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4">
                                                <div className="text-sm text-gray-900 max-w-xs">
                                                    {service.description}
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <span className="inline-flex px-2 py-1 text-xs font-semibold rounded-full bg-gray-100 text-gray-800">
                                                    {service.port}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full border ${getStatusColor(service.status)}`}>
                                                    {service.status.toUpperCase()}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="flex items-center">
                                                    <div className="w-16 bg-gray-200 rounded-full h-2 mr-2">
                                                        <div
                                                            className={`h-2 rounded-full ${parseFloat(service.uptime) > 99 ? 'bg-green-600' :
                                                                parseFloat(service.uptime) > 95 ? 'bg-yellow-600' :
                                                                    'bg-red-600'
                                                                }`}
                                                            style={{ width: service.uptime }}
                                                        ></div>
                                                    </div>
                                                    <span className="text-sm text-gray-900">{service.uptime}</span>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                                                {service.responseTime}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                                {service.lastCheck}
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>

                    {/* Action Buttons */}
                    <div className="mt-6 flex justify-end space-x-3">
                        <button className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                            </svg>
                            Refresh Status
                        </button>
                        <button className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                            Export Report
                        </button>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default SystemHealth;
