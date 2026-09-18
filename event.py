# event handling function

import datetime

db = {}

#add event

def add_event():
    event_name = input('Enter the event name: ')
    event_date_str = input('Enter the event date (YYYY-MM-DD): ')
    event_time_str = input('Enter the event time (HH:MM): ')

    try:
        event_date = datetime.datetime.strptime(event_date_str, '%Y-%m-%d').date()
        event_time = datetime.datetime.strptime(event_time_str, '%H:%M').time()
        event_datetime = datetime.datetime.combine(event_date, event_time)
        print(f'Event "{event_name}" added for {event_datetime}.')
    except ValueError:
        print('Invalid date or time format. Please try again.')

#key: value pair in db
#key event name event date 

def add_event_to_db(event_name, event_datetime):
    db[event_name] = event_datetime



#list event

def list_events():
    print('List Events')
    for event_name, event_datetime in db.items():
        print(f' - {event_name}: {event_datetime}')

#quit application

#prompt the user for imput

def main():
    while True:
        print('\n Event Management Syestem')
        print('1. Add Event')
        print('2. List Events')
        print('3. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            print('Add Event')
            add_event()
        elif choice == '2':
            print('List Events')
        elif choice == '3':
            print('✌️ Goodbye!')
    
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()

