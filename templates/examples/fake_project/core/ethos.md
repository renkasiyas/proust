# ACME Corp Widget Platform Ethos

## Core Philosophy
Building enterprise-grade widget management software that scales with organizations while maintaining simplicity for end users. We believe powerful tools should feel effortless.

## Memory-First Development
Every interaction builds upon previous context. The AI maintains deep awareness of:
- Widget taxonomy and business rules established in v1.0
- Customer integration patterns from 200+ deployments
- Performance bottlenecks identified in Q3 scaling issues
- Support escalation patterns and resolution workflows

## Values
- **Security over convenience**: Enterprise data demands robust protection
- **Performance at scale**: Sub-100ms response times even with 10M+ widgets
- **API-first design**: Headless architecture enables customer integrations
- **Backwards compatibility**: Never break existing customer implementations

## Decision Framework
When facing architectural or design decisions:
1. Does this maintain API contract stability?
2. Will this perform under enterprise load (1M+ widgets)?
3. Can customer security teams approve this approach?
4. Does this reduce operational overhead for our SRE team?

## Quality Standards
- 99.9% API uptime SLA with enterprise customers
- Sub-100ms P95 response times for all read operations
- 95%+ test coverage on business logic and API contracts
- SOC 2 Type II compliance for data handling
- Zero-downtime deployments for all production changes

## Team Working Principles
- **Communication**: Async-first with daily standups for blockers only
- **Code Review**: Required approval from domain expert + security review for API changes
- **Testing**: TDD for business logic, integration tests for all API endpoints
- **Deployment**: Blue-green deployments with automated rollback triggers

*This ethos guides all development decisions and AI behavior within the ACME Widget Platform.*