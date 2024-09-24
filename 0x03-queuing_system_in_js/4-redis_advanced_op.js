import redis from 'redis';

const client = redis.createClient();

const data = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

for (const d in data) {
  client.hset('HolbertonSchools', d, data[d], redis.print);
};

client.hgetall('HolbertonSchools', (error, reply) => {
  console.log(reply);
});
