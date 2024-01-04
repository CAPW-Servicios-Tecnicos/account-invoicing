import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-account-invoicing",
    description="Meta package for oca-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_billing',
        'odoo14-addon-account_global_discount',
        'odoo14-addon-account_invoice_alternate_payer',
        'odoo14-addon-account_invoice_base_invoicing_mode',
        'odoo14-addon-account_invoice_blocking',
        'odoo14-addon-account_invoice_change_currency',
        'odoo14-addon-account_invoice_check_picking_date',
        'odoo14-addon-account_invoice_check_total',
        'odoo14-addon-account_invoice_date_due',
        'odoo14-addon-account_invoice_discount_display_amount',
        'odoo14-addon-account_invoice_fiscal_position_update',
        'odoo14-addon-account_invoice_fixed_discount',
        'odoo14-addon-account_invoice_force_number',
        'odoo14-addon-account_invoice_line_description',
        'odoo14-addon-account_invoice_line_sequence',
        'odoo14-addon-account_invoice_mass_sending',
        'odoo14-addon-account_invoice_merge',
        'odoo14-addon-account_invoice_mode_at_shipping',
        'odoo14-addon-account_invoice_mode_daily',
        'odoo14-addon-account_invoice_mode_monthly',
        'odoo14-addon-account_invoice_mode_weekly',
        'odoo14-addon-account_invoice_partner',
        'odoo14-addon-account_invoice_payment_retention',
        'odoo14-addon-account_invoice_pricelist',
        'odoo14-addon-account_invoice_pricelist_sale',
        'odoo14-addon-account_invoice_refund_line_selection',
        'odoo14-addon-account_invoice_refund_link',
        'odoo14-addon-account_invoice_refund_reason',
        'odoo14-addon-account_invoice_refund_reason_skip_anglo_saxon',
        'odoo14-addon-account_invoice_refund_reinvoice',
        'odoo14-addon-account_invoice_restrict_linked_so',
        'odoo14-addon-account_invoice_search_by_reference',
        'odoo14-addon-account_invoice_section_picking',
        'odoo14-addon-account_invoice_section_sale_order',
        'odoo14-addon-account_invoice_supplier_ref_unique',
        'odoo14-addon-account_invoice_supplier_self_invoice',
        'odoo14-addon-account_invoice_supplierinfo_update',
        'odoo14-addon-account_invoice_supplierinfo_update_discount',
        'odoo14-addon-account_invoice_tax_note',
        'odoo14-addon-account_invoice_tax_required',
        'odoo14-addon-account_invoice_transmit_method',
        'odoo14-addon-account_invoice_tree_currency',
        'odoo14-addon-account_invoice_triple_discount',
        'odoo14-addon-account_invoice_validation_queued',
        'odoo14-addon-account_invoice_view_payment',
        'odoo14-addon-account_mail_autosubscribe',
        'odoo14-addon-account_menu_invoice_refund',
        'odoo14-addon-account_move_exception',
        'odoo14-addon-account_move_line_accounting_description',
        'odoo14-addon-account_move_line_accounting_description_purchase',
        'odoo14-addon-account_move_line_accounting_description_sale',
        'odoo14-addon-account_move_original_partner',
        'odoo14-addon-account_move_post_block',
        'odoo14-addon-account_move_propagate_ref',
        'odoo14-addon-account_move_tier_validation',
        'odoo14-addon-account_move_tier_validation_approver',
        'odoo14-addon-account_move_tier_validation_forward',
        'odoo14-addon-account_receipt_journal',
        'odoo14-addon-account_receipt_print',
        'odoo14-addon-account_refund_payment_term',
        'odoo14-addon-accounting_partner_category',
        'odoo14-addon-product_supplierinfo_for_customer_invoice',
        'odoo14-addon-purchase_stock_picking_return_invoicing',
        'odoo14-addon-sale_line_refund_to_invoice_qty',
        'odoo14-addon-sale_line_refund_to_invoice_qty_skip_anglo_saxon',
        'odoo14-addon-sale_order_invoicing_grouping_criteria',
        'odoo14-addon-sale_order_invoicing_qty_percentage',
        'odoo14-addon-sale_order_invoicing_queued',
        'odoo14-addon-sale_timesheet_invoice_description',
        'odoo14-addon-stock_picking_invoicing',
        'odoo14-addon-stock_picking_invoicing_incoterm',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
