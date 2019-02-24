# 301remover-rpc-server

Part of the 301remover project.

This component handles querying the database ([LMDB](https://symas.com/lmdb/)) for shortcode mappings and resolving new shortcodes from URL shorteners. It connects with the main 301remover server via a [RabbitMQ](https://www.rabbitmq.com/) RPC.
