---
layout: default
title: Docker Compose Execution Report
---

# Docker Compose Execution Report

## Application Status
{%- if app_status -%}
{{ app_status }}
{%- endif -%}

## Monitoring Status
{%- if monitoring_status -%}
{{ monitoring_status }}
{%- endif -%}

## Container Logs
{%- if container_logs -%}
```
{{ container_logs }}
```
{%- endif -%}

## Health Checks
{%- if health_checks -%}
{{ health_checks }}
{%- endif -%}