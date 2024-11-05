
# 1 - Levantamento de uma base histórica de clientes
Para este estudo usaremos a base da tabela de *asset_trade_bills* para identificar os clientes com o mesmo padrão. O objetivo é definir quais serão os critérios para identificar um cliente bom ou ruim.
A base de asset_trade_bills possui 15 colunas, sendo:
1. id
2. due_date
3. nfe_number
4. nfe_series
5. kind
6. state
7. payer_id
8. endorser_original_id
9. new_due_date
10. participant_id
11. ballast_kind
12. invoice_number
13. payment_place
14. update_reason_kind
15. finished_at

Para definidor critérios para avaliar os clientes com histórico, será agrupado as informações por endossante (*endorser_original_id*), no qual será considerado:
- Duplicatas encerradas (**state**: *finished* ou *canceled*)
- Renegociações de prazo de pagamento.
- Área de negociação: Produtos ou serviços.
- Local de Pagamento: Cidade e Estado.