# IPFS Control Panel Requirements Document

## Overview

The IPFS Control Panel is a web-based security analyst interface for monitoring and managing IPFS threat detection activities. Based on the existing system architecture, this document outlines the comprehensive requirements for building a modern, secure, and feature-rich control panel.

## 1. Authentication & Authorization

### 1.1 User Authentication
- **Mandatory Login**: All users must authenticate before accessing any functionality
- **Login Methods**:
  - Username/Password authentication (username: ipfs, password: 926Ehkry46LY)
- **Session Management**:
  - Configurable session timeout (default: 8 hours)
  - Secure session tokens with automatic refresh
  - Logout functionality with session invalidation

## 2. Phishing CID Management

### 2.1 Phishing CID List View
- **Display Requirements**:
  - Paginated list of confirmed phishing CIDs
  - Sortable columns: CID, Detection Date, Campaign, Source
  - Search functionality by: CID, Detection Date, Campaign, Source
- **Data Fields**:
  - CID (IPFS Content Identifier)
  - Detection timestamp
  - Campaign association
  - Source (bitswap vs PDNS vs both)

### 2.2 CID Detail View
- **Detailed Information Display**:
  - Full CID metadata and analysis results
  - Screenshot of the phishing page (Base64 encoded image)
  - HTML content analysis results
  - SimHash similarity matches
  - Detection confidence scores
  - Gateway information where CID was discovered
- **Interactive Features**:
  - Full-screen screenshot viewer
  - HTML source code viewer with syntax highlighting
  - Download original HTML content
  - Export CID details to PDF/CSV
- **Action Buttons**:
  - Confirm as phishing (Senior Analyst+)
  - Mark as false positive
  - Add to campaign
  - Share with external systems

## 3. Campaign Management

### 3.1 Campaign Overview
- **Campaign List**:
  - Display all identified phishing campaigns
  - Campaign metadata: Name, Start Date, End Date, CID Count, Status
  - Search and filter campaigns by name, date, or status
- **Campaign Creation**:
  - Manual campaign creation with custom names
  - Automatic campaign detection based on SimHash similarity
  - Campaign merging capabilities

### 3.2 Campaign Detail View
- **Campaign Information**:
  - Campaign name and description
  - Timeline of campaign activity
  - Geographic distribution of gateways
  - Threat evolution over time
- **Associated CIDs**:
  - List of all phishing CIDs in the campaign
  - CID similarity matrix
  - Common characteristics analysis
  - Campaign progression timeline

## 4. Analytics & Dashboards

### 4.1 Real-Time Monitoring Dashboard
- **Key Metrics Display**:
  - Total CIDs processed (24h, 7d, 30d)
  - Active campaigns count
  - System health status
  - Gateway discovery rate
  - Detection accuracy metrics

### 4.2 Threat Detection Analytics
- **CTI Detection Graphs**:
  - Daily/weekly/monthly CTI detection trends
  - CTI detection by gateway source
  - Password field detection patterns
  - Geographic distribution of CTI detections
- **Obfuscation Detection Analytics**:
  - JavaScript-heavy content trends
  - Obfuscation techniques evolution
  - Detection confidence distribution
  - False positive rates

### 4.3 Network Flow Analytics
- **Bitswap Flow Monitoring**:
  - IPFS network traffic patterns
  - Content retrieval success rates
  - Network performance metrics
  - Gateway response times
- **PDNS Flow Analysis**:
  - PassiveDNS query patterns
  - Gateway discovery trends
  - Domain resolution analytics
  - DNS query volume over time

### 4.4 SimHash Analytics
- **Similarity Detection**:
  - New SimHash CIDs discovered
  - Similarity cluster analysis
  - Content evolution tracking
  - Malware family identification
- **Hash Database Management**:
  - SimHash database statistics
  - Similarity threshold tuning
  - Hash collision analysis
  - Database growth trends

### 4.5 Customizable Dashboards
- **Widget-Based Interface**:
  - Drag-and-drop dashboard builder
  - Customizable chart types (line, bar, pie, heatmap)
  - Real-time data refresh options
  - Export dashboard as PDF/image
- **Predefined Dashboard Templates**:
  - Executive Summary Dashboard
  - Technical Operations Dashboard
  - Threat Intelligence Dashboard
  - System Health Dashboard

## 5. System Health & Monitoring

### 5.1 Service Health Monitoring
- **Component Status**:
  - CID Notify Service (Port 9090)
  - Gateway Server (Port 9191)
  - PDNS Processor (Port 9393)
  - Control Panel API (Port 6655)
  - MongoDB Database
- **Health Indicators**:
  - Service availability (Healthy/Unhealthy/Unreachable)
  - Response time metrics
  - Error rate monitoring
  - Resource utilization

### 5.2 Gateway Management
- **Gateway List**:
  - Display all discovered IPFS gateways
  - Gateway status and response times
  - Geographic location of gateways
  - Gateway reliability metrics
- **Gateway Operations**:
  - Add/remove gateways manually
  - Test gateway connectivity
  - Gateway performance monitoring
  - Gateway categorization

## 6. Data Management & Storage

### 6.1 Database Schema Extensions
- **User Management Tables**:
  - `users`: User accounts and authentication
  - `user_roles`: Role assignments
  - `user_sessions`: Active sessions
- **Campaign Management**:
  - `campaigns`: Campaign metadata
  - `campaign_cids`: CID-campaign associations
- **Analytics Data**:
  - `detection_metrics`: Daily detection statistics
  - `system_health_logs`: Health monitoring data
  - `user_activity_logs`: User action tracking

### 6.2 Data Retention & Archival
- **Retention Policies**:
  - Raw detection data: 90 days
  - Confirmed phishing CIDs: 2 years
  - System logs: 30 days
  - User activity logs: 1 year
- **Data Export**:
  - Bulk export of CID data
  - Campaign data export
  - System metrics export
  - Compliance reporting

## 7. User Interface Requirements

### 7.1 Design Standards
- **Modern Web Interface**:
  - Responsive design for desktop and tablet
  - Dark/light theme support
  - Accessibility compliance (WCAG 2.1)
  - Mobile-friendly navigation
- **Technology Stack**:
  - Frontend: React.js with Material-UI or similar
  - Charts: Chart.js, D3.js, or Recharts
  - State Management: Redux or Context API
  - HTTP Client: Axios with interceptors

### 7.2 Navigation & Layout
- **Main Navigation**:
  - Dashboard (default landing page)
  - Phishing CIDs
  - Campaigns
  - Analytics
  - System Health
  - Settings (Admin only)
- **Breadcrumb Navigation**:
  - Clear navigation path indication
  - Quick access to parent pages
- **Search & Filter**:
  - Global search across all data
  - Advanced filtering options
  - Saved search queries

## 8. API Requirements

### 8.1 RESTful API Extensions
- **Authentication Endpoints**:
  - `POST /api/auth/login`
  - `POST /api/auth/logout`
  - `GET /api/auth/me`
  - `POST /api/auth/refresh`
- **Campaign Management**:
  - `GET /api/campaigns`
  - `POST /api/campaigns`
  - `GET /api/campaigns/{id}`
  - `PUT /api/campaigns/{id}`
  - `GET /api/campaigns/{id}/cids`
- **Analytics Endpoints**:
  - `GET /api/analytics/cti-trends`
  - `GET /api/analytics/obfuscation-stats`
  - `GET /api/analytics/bitswap-flow`
  - `GET /api/analytics/pdns-flow`
  - `GET /api/analytics/simhash-stats`

### 8.2 Real-Time Updates
- **WebSocket Integration**:
  - Real-time CID detection notifications
  - Live system health updates
  - Campaign activity notifications
  - User activity indicators

## 9. Security Requirements

### 9.1 Data Security
- **Encryption**:
  - HTTPS/TLS for all communications
  - Encrypted data at rest
  - Secure session management
- **Input Validation**:
  - SQL injection prevention
  - XSS protection
  - CSRF protection
  - Input sanitization

### 9.2 Audit & Compliance
- **Audit Logging**:
  - User login/logout events
  - CID confirmation actions
  - Campaign modifications
  - System configuration changes
- **Compliance Features**:
  - Data retention compliance
  - Privacy protection measures
  - Export capabilities for compliance reporting

## 10. Performance Requirements

### 10.1 Response Times
- **Page Load Times**:
  - Dashboard: < 2 seconds
  - CID list: < 3 seconds
  - CID detail view: < 2 seconds
  - Analytics charts: < 5 seconds
- **API Response Times**:
  - Authentication: < 500ms
  - Data queries: < 1 second
  - File uploads: < 10 seconds

### 10.2 Scalability
- **Concurrent Users**:
  - Support 50+ concurrent users
  - Horizontal scaling capability
  - Database optimization for large datasets
- **Data Volume**:
  - Handle 100,000+ CIDs
  - Support 1,000+ campaigns
  - Efficient pagination and filtering

## 11. Integration Requirements

### 11.1 External System Integration
- **Threat Intelligence Feeds**:
  - Integration with external TI platforms
  - Automated threat sharing
  - IOCs export capabilities
- **Notification Systems**:
  - Email notifications for critical alerts
  - Slack/Teams integration
  - SMS alerts for urgent threats

### 11.2 Data Export/Import
- **Export Formats**:
  - CSV for data analysis
  - JSON for API integration
  - PDF for reporting
  - STIX/TAXII for threat sharing
- **Import Capabilities**:
  - Bulk CID import
  - Campaign data import
  - User management import

## 12. Deployment & Operations

### 12.1 Deployment Requirements
- **Container Support**:
  - Docker containerization
  - Kubernetes deployment ready
  - Environment-specific configurations
- **Database Requirements**:
  - MongoDB cluster support
  - Database backup and recovery
  - Connection pooling

### 12.2 Monitoring & Alerting
- **Application Monitoring**:
  - Performance metrics collection
  - Error tracking and alerting
  - User activity monitoring
- **Infrastructure Monitoring**:
  - Server resource monitoring
  - Database performance tracking
  - Network connectivity monitoring

## 13. Testing Requirements

### 13.1 Testing Strategy
- **Unit Testing**:
  - 80%+ code coverage
  - API endpoint testing
  - Component testing
- **Integration Testing**:
  - End-to-end user workflows
  - Database integration testing
  - External service integration testing
- **Security Testing**:
  - Penetration testing
  - Vulnerability scanning
  - Authentication testing

## 14. Documentation Requirements

### 14.1 User Documentation
- **User Manual**:
  - Feature overview and usage
  - Step-by-step workflows
  - Troubleshooting guide
- **API Documentation**:
  - OpenAPI/Swagger specification
  - Code examples
  - Authentication guide

### 14.2 Technical Documentation
- **System Architecture**:
  - Component diagrams
  - Data flow documentation
  - Deployment architecture
- **Development Documentation**:
  - Code style guidelines
  - Development setup
  - Contributing guidelines

## 15. Future Enhancements

### 15.1 Advanced Features
- **Machine Learning Integration**:
  - Automated threat classification
  - Predictive analytics
  - Anomaly detection
- **Advanced Analytics**:
  - Network graph visualization
  - Temporal analysis
  - Geographic threat mapping

### 15.2 Mobile Application
- **Mobile App Requirements**:
  - Native iOS/Android apps
  - Push notifications
  - Offline capability
  - Biometric authentication

## Implementation Priority

### Phase 1 (Core Functionality)
1. User authentication and authorization
2. Basic phishing CID management
3. Simple campaign management
4. Basic analytics dashboard
5. System health monitoring

### Phase 2 (Enhanced Features)
1. Advanced analytics and visualizations
2. Real-time updates
3. Advanced search and filtering
4. Data export capabilities
5. Mobile-responsive design

### Phase 3 (Advanced Features)
1. Machine learning integration
2. Advanced threat intelligence
3. Mobile applications
4. Advanced reporting
5. Third-party integrations

This requirements document provides a comprehensive foundation for building a modern, secure, and feature-rich IPFS control panel that meets the needs of security analysts while maintaining the existing system's functionality and data integrity.
