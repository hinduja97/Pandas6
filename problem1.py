def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id',inplace=True)
    person.drop_duplicates('email',inplace=True)
    print(type(person))
    print(person)