# Python - Object Relational Mapping (ORM)

This repository contains Python scripts demonstrating Object Relational Mapping (ORM) concepts using SQLAlchemy, a powerful Python SQL toolkit and Object Relational Mapper.

## Overview

Object Relational Mapping (ORM) is a programming technique for converting data between incompatible type systems, in object-oriented programming languages. In the context of databases, an ORM maps data between an object-oriented system and a relational database management system (RDBMS).

This directory (`0x0F-python-object_relational_mapping`) contains Python scripts and modules that demonstrate ORM concepts, including:

- Defining database models using SQLAlchemy's Declarative Base class
- Creating, reading, updating, and deleting (CRUD) database records using SQLAlchemy
- Defining relationships between database tables
- Querying databases using SQLAlchemy's Object-Relational Query Language (ORMQL)

## Contents

- `model_state.py`: Defines the `State` model class representing a state in the USA.
- `model_city.py`: Defines the `City` model class representing a city in the USA.
- `relationship_city.py`: Defines the `City` model class with a relationship to the `State` model class.
- `relationship_state.py`: Defines the `State` model class with a relationship to the `City` model class.
- `*fetch*` scripts: Scripts that perform CRUD operations on the database.
- `*model_*` scripts: Scripts that define database models and create database tables.
- `*relationship*` scripts: Scripts that demonstrate relationships between database models.

## Getting Started

1. Clone the repository:

2. Navigate to the `0x0F-python-object_relational_mapping` directory:

3. Ensure you have MySQL installed on your system and running.

4. Install the required dependencies:

5. Run the Python scripts as needed:


## Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Python.org](https://www.python.org/)
- [Stack Overflow](https://stackoverflow.com/) - For troubleshooting and asking questions

## Author

[Ezra Kessem](https://github.com/ezzkessem8)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


