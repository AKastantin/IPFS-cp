function Gateways() {
    return (
        <div className="bg-gray-50">
            {/* Main Content */}
            <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                <div className="px-4 py-6 sm:px-0">
                    {/* Page Header */}
                    <div className="mb-8">
                        <h1 className="text-3xl font-bold text-gray-900">Gateways</h1>
                        <p className="mt-2 text-gray-600">Monitor and manage IPFS gateway connections</p>
                    </div>

                    {/* Gateway Stats */}
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                        <div className="bg-white overflow-hidden shadow rounded-lg">
                            <div className="p-5">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <div className="w-8 h-8 bg-blue-500 rounded-md flex items-center justify-center">
                                            <span className="text-white font-bold">🌐</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Total Gateways</dt>
                                            <dd className="text-lg font-medium text-gray-900">47</dd>
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
                                            <span className="text-white font-bold">✅</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Online</dt>
                                            <dd className="text-lg font-medium text-gray-900">42</dd>
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
                                            <span className="text-white font-bold">❌</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Offline</dt>
                                            <dd className="text-lg font-medium text-gray-900">5</dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-white overflow-hidden shadow rounded-lg">
                            <div className="p-5">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <div className="w-8 h-8 bg-yellow-500 rounded-md flex items-center justify-center">
                                            <span className="text-white font-bold">⚡</span>
                                        </div>
                                    </div>
                                    <div className="ml-5 w-0 flex-1">
                                        <dl>
                                            <dt className="text-sm font-medium text-gray-500 truncate">Avg Response Time</dt>
                                            <dd className="text-lg font-medium text-gray-900">245ms</dd>
                                        </dl>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Search and Filter Bar */}
                    <div className="bg-white p-6 rounded-lg shadow mb-6">
                        <div className="flex flex-col sm:flex-row gap-4">
                            <div className="flex-1">
                                <input
                                    type="text"
                                    placeholder="Search gateways by URL or location..."
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                />
                            </div>
                            <div className="flex gap-2">
                                <select className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                                    <option>All Status</option>
                                    <option>Online</option>
                                    <option>Offline</option>
                                    <option>Slow</option>
                                </select>
                                <select className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                                    <option>All Regions</option>
                                    <option>North America</option>
                                    <option>Europe</option>
                                    <option>Asia</option>
                                </select>
                                <button className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition duration-200">
                                    Search
                                </button>
                                <button className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600 transition duration-200">
                                    Add Gateway
                                </button>
                            </div>
                        </div>
                    </div>

                    {/* Gateway List */}
                    <div className="bg-white shadow rounded-lg overflow-hidden">
                        <div className="px-6 py-4 border-b border-gray-200">
                            <h3 className="text-lg font-medium text-gray-900">Gateway List</h3>
                            <p className="text-sm text-gray-500">Showing all discovered gateways</p>
                        </div>

                        <div className="overflow-x-auto">
                            <table className="min-w-full divide-y divide-gray-200">
                                <thead className="bg-gray-50">
                                    <tr>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Gateway URL
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Location
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Status
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Response Time
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Reliability
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                            Actions
                                        </th>
                                    </tr>
                                </thead>
                                <tbody className="bg-white divide-y divide-gray-200">
                                    {/* Sample gateway data */}
                                    {[
                                        {
                                            url: 'https://ipfs.io',
                                            location: 'Global',
                                            status: 'Online',
                                            responseTime: '180ms',
                                            reliability: '98%'
                                        },
                                        {
                                            url: 'https://gateway.pinata.cloud',
                                            location: 'North America',
                                            status: 'Online',
                                            responseTime: '220ms',
                                            reliability: '95%'
                                        },
                                        {
                                            url: 'https://cloudflare-ipfs.com',
                                            location: 'Global',
                                            status: 'Online',
                                            responseTime: '195ms',
                                            reliability: '97%'
                                        },
                                        {
                                            url: 'https://dweb.link',
                                            location: 'Europe',
                                            status: 'Slow',
                                            responseTime: '850ms',
                                            reliability: '78%'
                                        },
                                        {
                                            url: 'https://ipfs.infura.io',
                                            location: 'North America',
                                            status: 'Offline',
                                            responseTime: 'N/A',
                                            reliability: '45%'
                                        }
                                    ].map((gateway, index) => (
                                        <tr key={index} className="hover:bg-gray-50">
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="text-sm font-medium text-gray-900">
                                                    {gateway.url}
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                                                {gateway.location}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${gateway.status === 'Online' ? 'bg-green-100 text-green-800' :
                                                    gateway.status === 'Slow' ? 'bg-yellow-100 text-yellow-800' :
                                                        'bg-red-100 text-red-800'
                                                    }`}>
                                                    {gateway.status}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                                                {gateway.responseTime}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="flex items-center">
                                                    <div className="w-16 bg-gray-200 rounded-full h-2 mr-2">
                                                        <div
                                                            className={`h-2 rounded-full ${parseFloat(gateway.reliability) > 90 ? 'bg-green-600' :
                                                                parseFloat(gateway.reliability) > 70 ? 'bg-yellow-600' :
                                                                    'bg-red-600'
                                                                }`}
                                                            style={{ width: gateway.reliability }}
                                                        ></div>
                                                    </div>
                                                    <span className="text-sm text-gray-900">{gateway.reliability}</span>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                                                <button className="text-blue-600 hover:text-blue-900 mr-3">
                                                    Test
                                                </button>
                                                <button className="text-green-600 hover:text-green-900 mr-3">
                                                    Configure
                                                </button>
                                                <button className="text-red-600 hover:text-red-900">
                                                    Remove
                                                </button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default Gateways;
