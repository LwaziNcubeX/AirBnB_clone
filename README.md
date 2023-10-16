![HBNB LOGO](https://github.com/LwaziNcubeX/AirBnB_clone/blob/main/hbnb.png?raw=true)

# HBNB AirBnB Clone - Command Line Interface

This project is a command line interface for interacting with a database of Airbnb-style rental properties. It is designed to be used with the HBNB AirBnB clone project, which provides a database of properties and a web interface for viewing and booking them.

## Command Interpreter

The command interpreter provides a variety of commands for creating, updating, and deleting objects in the database. It uses the argparse library to parse command line arguments and provide a user-friendly interface.

### Starting the Command Interpreter

To start the command interpreter, simply run the `console.py` file:

```
$ ./console.py
```

This will launch the command line interface and display a prompt:

```
(hbnb) 
```

### Using the Command Interpreter

The command interpreter provides a variety of commands for interacting with the database of rental properties. Here are some examples:

#### `help` Command

The `help` command displays a list of available commands and provides help on their usage:

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
```

To get help on a specific command, use the `help` command followed by the command name:

```
(hbnb) help create

        Create a new instance of BaseModel, save it (to the JSON file) and prints the id.

        Usage: create <class name>
```

#### `create` Command

The `create` command creates a new rental property object in the database. To use it, simply specify the class name and any desired attributes:

```
(hbnb) create Place

2da6d8b2-e164-4e03-9e1c-61180dd8a88c
```

This will create a new `Place` object in the database with the specified attributes and display its unique ID.

#### `show` Command

The `show` command displays the details of a specific rental property object. To use it, simply specify the class name and object ID:

```
(hbnb) show Place 2da6d8b2-e164-4e03-9e1c-61180dd8a88c

[Place] (2da6d8b2-e164-4e03-9e1c-61180dd8a88c) {'name': 'Cozy Cabin', 'city': 'Big Bear', 'price': 150}
```

This will display the details of the specified `Place` object.

#### `update` Command

The `update` command updates the attributes of a specific rental property object. To use it, simply specify the class name, object ID, and attributes to update:

```
(hbnb) update Place 2da6d8b2-e164-4e03-9e1c-61180dd8a88c name "Rustic Lodge"

(hbnb) show Place 2da6d8b2-e164-4e03-9e1c-61180dd8a88c

[Place] (2da6d8b2-e164-4e03-9e1c-61180dd8a88c) {'name': 'Rustic Lodge', 'city': 'Big Bear', 'price': 150}
```

This will update the `name` attribute of the specified `Place` object and display its updated details.

#### `destroy` Command

The `destroy` command deletes a specific rental property object from the database. To use it, simply specify the class name and object ID:

```
(hbnb) destroy Place 2da6d8b2-e164-4e03-9e1c-61180dd8a88c

(hbnb) show Place 2da6d8b2-e164-4e03-9e1c-61180dd8a88c

** no instance found **
```

This will delete the specified `Place` object from the database.

## Examples

Here are some example commands to get you started:

```
create BaseModel
create User 
show Place 1d227a9e-7f27-44c4-9725-00abfdbef03d
update User b900318d-d1ff-4f52-a8d3-fa4839e7bd23 password xyz9876
destroy Place 1d227a9e-7f27-44c4-9725-00abfdbef03d
