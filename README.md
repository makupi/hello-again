# 01 - Backend Optimisation: List & Search

Imagine the B2B Saas Dashboard from hello again. Businesses use it as a CRM,
communication/newsletter tool and also manage their loyalty assets.
One main use case of such a CRM is listing, searching & filtering for contacts.

Take the following data model, consisting of 3 tables as given:

```
AppUser
    id
    first_name
    last_name
    gender
    customer_id
    phone_number
    created
    address_id (FK)
    birthday
    last_updated
Address
    id
    street
    street_number
    city_code
    city
    country
CustomerRelationship
    id
    appuser_id (FK)
    points
    created
    last_activity
```

# Task
- Set up a Django project that reflects that data structure
- Write a script to insert ~3 Mio data entries (AppUser, Address and a Customer
Relationship) - you can use random values
- For the Database feel free to use your personal preference (Sqlite, Postgresql, etc.)
- Implement a View for the data structure that lists your entries. It should join all 3
tables, since the response should include attributes from all 3 tables
- The view should be able to sort, filter and list by any field
- The view should also come with pagination support
- Benchmark your view with certain queries (measure how long it takes to return
results)
    - E.g. Filter by a name
    - Sort by attribute
    - Load initial list including pagination
- Now think about performance optimisations and as a bonus, implement them and
compare them with your initial benchmarks


# Performance

Using `silk` profiler

- First thing I noticed is that `Paginator` will count all elements before the actual query, if we're filtering by e.g. `first_name` SQL will have to do a full row scan which results in a rather slow query.
    - Query: http://127.0.0.1:8000/crm/appusers?first_name=Steve&page=10
    - Solution: Add indices for commonly filtered columns
        `CREATE INDEX crm_appuser_first_name ON crm_appuser(first_name);`
        - Impact: From ~450ms to 20ms spent on queries
- Django performs **77** queries to load the list, which could impact the performance
    - Query: http://127.0.0.1:8000/crm/appusers?first_name=Steve&page=10
    - Solution: Add `select_related("address")`
        - Impact: Queries reduced from **77** to **52**, average overall time reduced by ~5-10ms
    - Solution 2: Also add `prefetch_related("customerrelationship_set")`
        - Impact: Queries increased from **52** to **53**
        - Note:  Currently this doesn't really have an impact on performance since the database was only populated with a 1:1 relationship between appuser and cr, if there were multiple cr columns per appuser this could provide a bigger impact
    