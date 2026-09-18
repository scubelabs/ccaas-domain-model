# Notification Domain

Notification is platform-to-user/agent/supervisor communication distinct from customer interaction messages.

Core concepts: Notification, Template, TemplateVersion, Recipient, DeliveryChannel, DeliveryAttempt and Preference.

Examples include agent offer alerts, supervisor alerts, WFM schedule changes and system notifications.

Templates are versioned; deliveries reference the rendered template/version. Delivery attempts preserve provider reference, timestamps and terminal outcome.

Preferences and mandatory operational notifications are distinct policy categories. Sensitive payloads should be minimized because push/email notification channels may expose content outside the core application.
