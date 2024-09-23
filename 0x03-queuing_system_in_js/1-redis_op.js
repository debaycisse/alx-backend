import { createClient, print } from "redis";

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, res) => {
    if (error) throw new Error(error.message);
    print(`Reply: ${res}`);
  });
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, res) => {
    if (error) {
      throw new Error(error.message)
    };
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
