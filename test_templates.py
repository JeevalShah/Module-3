from template_system import TemplateManager

tm = tm = TemplateManager("template_system/message_templates.json")

customer_data = {
    "name": "Rahul",
    "offer": "20% OFF on all orders",
    "due_amount": "500",
    "announcement": "We are launching a new menu this weekend!"
}

offer_msg = tm.generate_message("offer_message", customer_data)
repeat_msg = tm.generate_message("repeat_order_message", customer_data)
announce_msg = tm.generate_message("announcement_message", customer_data)
payment_msg = tm.generate_message("payment_reminder_message", customer_data)

print("Offer Message:\n", offer_msg)
print()
print("Repeat Order Message:\n", repeat_msg)
print()
print("Announcement Message:\n", announce_msg)
print()
print("Payment Reminder:\n", payment_msg)