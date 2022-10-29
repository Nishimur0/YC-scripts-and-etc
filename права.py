print("введи user_id")
user_id = input() #задали user_id
print("введи филиалы в формате '1, 2, 3'")
salon_id = input() #Задали список филиалов через запятую
list = salon_id.split() #указал, что загруженные филиалы являются списком (после запятой, пробел обязателен)
print("внеси шаблон прав (скопировать из БД только значения, кроме user_id, salon_id) через запятую")
shablon = input() #Шаблон для user_salon_link
print("Внеси шаблон для user_notification_settings (только status и status_by_permissions) через запятую")
shablon2 = input() #Шаблон для user_notification_settings
print("Внеси шаблоны, каждый на новой строке, для user_notification_type_settings через запятую") 
shablon3, shablon4, shablon5, shablon6, shablon7 = input(), input(), input(), input(), input() #Шаблоны User_notifications_types
s = ("values")
with open('users_salon_link.sql', 'w') as f:
    print("insert into users_salons_link (user_id, salon_id, user_role_id, "
      "`group`, stat_access, clients_access, clients_loyalty_read_access, "
      "clients_phones_email_access, clients_card_phone_access, clients_excel_access, "
      "clients_delete_access, settings_access, dash_access, dash_phones_access, dashboard_access, "
      "dash_records_access, dash_records_last_days_count, dash_records_excel_access, "
      "dash_records_phones_access, dash_message_access, dash_message_excel_access, dash_message_phones_access, "
      "dash_reviews_access, dash_reviews_delete_access, record_form_access, record_form_client_access, "
      "record_form_client_add_access, records_autocomplete_access, records_autocomplete_phone_access, "
      "edit_records_access, edit_records_attendance_access, records_services_cost_access, "
      "records_services_discount_access, delete_records_access, delete_paid_records_access, "
      "delete_customer_came_records_access, records_goods_access, storages_goods_units_edit_access, "
      "records_goods_edit_transaction_access, records_goods_create_transaction_access, "
      "records_goods_cost_access, records_goods_discount_access, records_finances_access, "
      "records_finances_last_days_count, records_finances_pay_from_deposits_access, records_group_id, "
      "timetable_access, timetable_phones_access, create_records_access, billing_access, send_sms, "
      "salon_to_salon_group_add_access, users_access, services_delete, services_edit, "
      "settings_services_create_access, settings_services_edit_services_related_resource_access, "
      "settings_services_edit_online_pay_access, settings_services_edit_online_seance_date_time_access, "
      "settings_services_edit_image_access, settings_services_edit_price_access, "
      "settings_services_relation_category_access, settings_services_edit_title_access, master_delete,"
      " master_edit, schedule_edit, excel_access, client_phones_access, master_id, position_id, "
      "finances_access, finances_payroll_calculation_create_by_master_access, "
      "finances_payroll_calculation_create_access, finances_accounts_limited_access, "
      "finances_accounts_ids, finances_transactions_access, finances_transactions_excel_access, "
      "finances_create_last_days_count, finances_create_transactions_access, finances_edit_transactions_access, "
      "finances_delete_transactions_access, finances_last_days_count, finances_edit_last_days_count, "
      "finances_expenses_limited_access, finances_expenses_ids, finances_accounts_access, "
      "finances_accounts_banalce_access, finances_salary_schemes_access, finances_salary_calc_access, "
      "finances_salary_pay_access, finances_period_report_access, finances_period_report_excel_access, "
      "finances_year_report_access, finances_year_report_excel_access, storages_access, storages_limited_access, "
      "storages_ids, storages_move_goods_access, storages_transactions_types_limited_access, "
      "storages_transactions_types, storages_transactions_access, storages_transactions_excel_access, "
      "storages_create_transactions_sale_access, storages_create_transactions_buy_access, s"
      "torages_create_last_days_count, storages_create_transactions_access, storages_edit_transactions_access, "
      "storages_edit_transactions_buy_access, storages_edit_transactions_sale_access, "
      "storages_delete_transactions_access, storages_remnants_report_access, storages_inventory_access,"
      " storages_inventory_create_edit_access, storages_inventory_delete_access, storages_inventory_excel_access, "
      "storages_remnants_report_excel_access, storages_sales_report_access, storages_sales_report_excel_access, "
      "storages_last_days_count, schedule_edit_access, last_days_count, non_deletable_user, push, web_push, "
      "web_phone_push, storages_consumable_report_access, storages_consumable_report_excel_access, loyalty_access, "
      "loyalty_cards_manual_transactions_access, loyalty_cards_issue_and_removal_access, "
      "loyalty_certificate_and_abonement_manual_transactions_access, storages_turnover_report_access, "
      "storages_turnover_report_excel_access, clients_visit_master_id, storages_edit_last_days_count, "
      "records_goods_edit_last_days_count, records_goods_create_last_days_count, client_comments_list_access, "
      "client_comments_add_access, client_comments_own_edit_access, client_comments_other_edit_access, "
      "client_files_list_access, client_files_upload_access, client_files_delete_access, auth_list_allowed_ip, "
      "auth_enable_check_ip, storages_goods_crud_access, storages_goods_create_access, storages_goods_update_access,"
      " storages_goods_cost_price_edit_access, storages_goods_comment_edit_access, "
      "storages_goods_masses_edit_access, storages_goods_critical_balance_edit_access, "
      "storages_goods_selling_price_edit_access, storages_goods_category_edit_access, "
      "storages_goods_title_edit_access, storages_goods_archive_access, storages_goods_delete_access, "
      "finances_salary_access_master_id, finances_print_check_access, finances_suppliers_read_access, "
      "finances_suppliers_create_access, finances_suppliers_update_access, finances_suppliers_delete_access, "
      "finances_suppliers_excel_access, finances_expenses_read_access, finances_expenses_create_access, "
      "finances_expenses_update_access, finances_expenses_delete_access, finances_options_read_access, "
      "finances_options_update_access, finances_kkm_transactions_access, finances_kkm_settings_read_access, "
      "finances_kkm_settings_update_access, finances_settings_invoicing_read_access, "
      "finances_settings_invoicing_update_access, timetable_transferring_record_access, "
      "edit_master_service_and_duration, tech_card_edit, limited_users_access, delete_users_access, "
      "create_users_access, edit_users_access, notification, notification_sms_ending_license, "
      "notification_sms_low_balance, notification_email_ending_license, timetable_statistics_access, "
      "webhook_read_access, storages_write_off_report_access, storages_write_off_report_excel_access, "
      "dashboard_calls_access, dashboard_calls_phones_access, settings_basis_access, settings_information_access, "
      "settings_notifications_access, settings_template_notifications_access, settings_services_access, "
      "settings_master_access, settings_master_dismiss_access, dashboard_calls_excel_access, master_create, "
      "finances_salary_not_limitation_today_access, "
      "finances_payroll_calculation_create_not_limitation_today_access, "
      "finances_salary_master_not_limitation_today_access, "
      "calculation_create_by_master_not_limitation_today_access, "
      "finances_z_report_access, finances_z_report_no_limit_today_access, "
      "finances_z_report_excel_access, settings_email_notifications_access, "
      "settings_positions_read, settings_positions_create, settings_positions_delete, "
      "billing_invoices_access, custom_fields_record_values_read_access, "
      "custom_fields_record_values_edit_access, custom_fields_client_values_read_access, "
      "custom_fields_client_values_edit_access, record_edit_full_paid_client_came_access, "
      "record_edit_full_paid_client_confirm_access, online_record_access, "
      "online_record_business_card_access, online_record_privacy_policy_access, "
      "settings_user_notifications_access, notifications_client_show, "
      "clients_show_attendance_history_access, clients_deposits_access, "
      "clients_deposits_create_access, clients_deposits_topup_access, clients_deposits_history_access, "
      "loyalty_abonement_balance_edit_access, loyalty_abonement_period_edit_access, "
      "loyalty_abonement_history_access, loyalty_certificate_balance_edit_access, "
      "loyalty_certificate_period_edit_access, online_record_chat_bot_access, is_approved, "
      "integration_wizard_access, integration_wizard_google_maps_access, records_consumables_edit, "
      "settings_close_docs_access, tips_access, tips_setup_access)", file=f)
    print(s, file=f)  # выводим команду
    for i in range(len(list)):  # задаем количество строк = количество филиалов в списке
        a = list[i]
        if "," in a:
            a = a[:len(a) - 1]  # убираем запятые из списка, если они есть
        print("(", user_id, ", ", a, ", ", shablon, ")", ",", sep="", file=f)  # выводим все "value"
with open('user_notification_settings.sql', 'w') as q:
    print("insert into user_notification_settings (id, salon_id, user_id, status, status_by_permissions)", file=q)
    print(s, file=q)
    for i in range(len(list)):  # задаем количество строк = количество филиалов в списке
        a = list[i]
        if "," in a:
            a = a[:len(a) - 1]  # убираем запятые из списка, если они есть
        print("(","NULL",",", a, ", ", user_id, ", ", shablon2, ")", ",", sep="", file=q)  # выводим все "value"
with open('users_notifi_type.sql', 'w') as p:
    print("insert into user_notification_type_settings (id, salon_id, user_id, type, enabled, push, vk, sms, email)", file = p)
    print(s, file = p)
    for i in range(len(list)):  # задаем количество строк = количество филиалов в списке
        a = list[i]
        if "," in a:
            a = a[:len(a) - 1]  # убираем запятые из списка, если они есть
        print("(","NULL",",", a, ", ", user_id, ", ", shablon3, ")",",",sep="", file=p)
        print("(", "NULL", ",", a, ", ", user_id, ", ", shablon4, ")",",", sep="", file=p)
        print("(", "NULL", ",", a, ", ", user_id, ", ", shablon5, ")",",", sep="", file=p)
        print("(", "NULL", ",", a, ", ", user_id, ", ", shablon6, ")",",", sep="", file=p)
        print("(", "NULL", ",", a, ", ", user_id, ", ", shablon7, ")",",", sep="", file=p)