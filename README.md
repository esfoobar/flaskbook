# Step 1

## Introduction to MongoDB

- Databases and Collections
- Indexes
- Documents
- ObjectId's

## Setting up MongoDB on Cloud9

- Cloud9 comes pre-installed with MongoDB. 
- To set it up you need to create a data directory: `mkdir ~/data`
- You also need a log directory: `mkdir ~/log`
- Create the mongodb config
- Start the client with `mongod -f mongod.conf`

## Playing with MongoDB
- Create a database by inserting a record: `db.test.insert({name: "Jorge", last_name: "Escobar"})`
- Show the record by doing a find: `db.test.find()`
- Insert another record and do another find
- Do a find for a specific record: `db.test.find({last_name:"Escobar"})`
- Create an index: `db.records.createIndex( { last_name: 1 } )`
- Insert another document, completely different schema: `db.test.insert({name: "Juan", last_name: "Escobar", age: 47})`
- Find that the record is still found: `db.test.find({last_name:"Escobar"})`
- You can also do documents inside of documents: `db.test.insert({name: {first_name: "Ricardo", last_name: "Escobar"}, age: 23})`
- That third record is *not* found: `db.test.find({last_name:"Escobar"})`
- You can do conditional searches: `db.test.find( { age: { $lt: 40 } } )` 
- You can do AND searches: `db.test.find( { name: "Jorge", last_name: "Escobar" } )`
- Update a record: 
```javascript 
db.test.update(
    { name: "Jorge" },
    {
      $set: {
        last_name: "Gonzalez"
      }
    }
)
```

## MongoDB Python ORM
- We'll be using MongoEngine to interact with MongoDB from our Python application