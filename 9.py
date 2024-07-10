import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def refresh_contacts_listbox():
    contacts_listbox.delete(0, tk.END)

    for contact in contacts:
        contacts_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == '' or phone == '':
        messagebox.showerror('Error', 'Please enter at least name and phone number')
        return

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(new_contact)

    messagebox.showinfo('Success', 'Contact added successfully')

    refresh_contacts_listbox()

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    search_name = simpledialog.askstring('Search Contact', 'Enter name to search:')
    if search_name:
        found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

        contacts_listbox.delete(0, tk.END)  

        if found_contacts:
            for contact in found_contacts:
                contacts_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            messagebox.showinfo('Search', f'No contacts found with name: {search_name}')

def update_contact():
    search_name = simpledialog.askstring('Update Contact', 'Enter name of contact to update:')
    if search_name:
        found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

        if found_contacts:
            contact = found_contacts[0]
            update_window = tk.Toplevel(root)
            update_window.title('Update Contact')

            update_name_label = tk.Label(update_window, text='Name:')
            update_name_label.grid(row=0, column=0, padx=10, pady=5)
            update_name_entry = tk.Entry(update_window, width=30)
            update_name_entry.grid(row=0, column=1, padx=10, pady=5)
            update_name_entry.insert(tk.END, contact['name'])

            update_phone_label = tk.Label(update_window, text='Phone:')
            update_phone_label.grid(row=1, column=0, padx=10, pady=5)
            update_phone_entry = tk.Entry(update_window, width=30)
            update_phone_entry.grid(row=1, column=1, padx=10, pady=5)
            update_phone_entry.insert(tk.END, contact['phone'])

            update_email_label = tk.Label(update_window, text='Email:')
            update_email_label.grid(row=2, column=0, padx=10, pady=5)
            update_email_entry = tk.Entry(update_window, width=30)
            update_email_entry.grid(row=2, column=1, padx=10, pady=5)
            update_email_entry.insert(tk.END, contact['email'])

            update_address_label = tk.Label(update_window, text='Address:')
            update_address_label.grid(row=3, column=0, padx=10, pady=5)
            update_address_entry = tk.Entry(update_window, width=30)
            update_address_entry.grid(row=3, column=1, padx=10, pady=5)
            update_address_entry.insert(tk.END, contact['address'])

            def perform_update():
                updated_name = update_name_entry.get()
                updated_phone = update_phone_entry.get()
                updated_email = update_email_entry.get()
                updated_address = update_address_entry.get()

                if updated_name == '' or updated_phone == '':
                    messagebox.showerror('Error', 'Please enter at least name and phone number')
                    return

                contact['name'] = updated_name
                contact['phone'] = updated_phone
                contact['email'] = updated_email
                contact['address'] = updated_address

                messagebox.showinfo('Success', 'Contact updated successfully')
                update_window.destroy()

                refresh_contacts_listbox()

            update_button = tk.Button(update_window, text='Update Contact', command=perform_update)
            update_button.grid(row=4, column=0, columnspan=2, pady=10)

            update_window.resizable(False, False)
        else:
            messagebox.showinfo('Update Contact', f'No contact found with name: {search_name}')

def delete_contact():
    search_name = simpledialog.askstring('Delete Contact', 'Enter name of contact to delete:')
    if search_name:
        found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

        if found_contacts:
            contact = found_contacts[0]

            confirmation = messagebox.askyesno('Confirm Deletion', f'Are you sure you want to delete {contact["name"]}?')

            if confirmation:
                contacts.remove(contact)
                messagebox.showinfo('Success', f'Contact {contact["name"]} deleted successfully')

                refresh_contacts_listbox()
        else:
            messagebox.showinfo('Delete Contact', f'No contact found with name: {search_name}')

root = tk.Tk()
root.title('Contact Book')
root.geometry("700x650")


tk.Label(root, text='Name:').grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text='Phone:').grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text='Email:').grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text='Address:').grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)


contacts_listbox = tk.Listbox(root, height=15, width=60)
contacts_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


add_button = tk.Button(root, text='Add Contact', bg='green', fg='white', command=add_contact)
add_button.grid(row=5, column=0, padx=10, pady=10)

view_button = tk.Button(root, text='View Contacts', bg='blue', fg='white', command=refresh_contacts_listbox)
view_button.grid(row=5, column=1, padx=10, pady=10)

search_button = tk.Button(root, text='Search Contact', bg='orange', fg='white', command=search_contact)
search_button.grid(row=6, column=0, padx=10, pady=10)

update_button = tk.Button(root, text='Update Contact', bg='grey', fg='white', command=update_contact)
update_button.grid(row=6, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text='Delete Contact', bg='red', fg='white', command=delete_contact)
delete_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
