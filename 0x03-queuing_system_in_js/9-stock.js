const express = require('express');
import { createClient } from 'redis';
const util = require('util');

const client = createClient();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

const transformObjectKeys = (itemObj, itemObjKeyMap) => {
  const newObj = {};
  for (const key in itemObj) {
    if (Object.hasOwnProperty.call(itemObj, key)) {
      const newKey = itemObjKeyMap[key] || key;
      newObj[newKey] = itemObj[key];
    }
  }
  return newObj;
};

const getItemByid = (id) => {
  const prd = listProducts.filter((product) => product.id === id);
  if (prd) return prd[0];
  else return null;
};

const app = express();
const port = 1245;

const reserveStockById = (itemId, stock) => {
  const itemObjKeyMap = {
    id: 'itemId',
    name: 'itemName',
    price: 'price',
    stock: 'intialAvailableQuantity',
  };
  const itemTransformed = transformObjectKeys(stock, itemObjKeyMap);
  itemTransformed['currentQuantity'] = itemTransformed.intialAvailableQuantity;
  client.set(itemId, JSON.stringify(itemTransformed));
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = util.promisify(client.get).bind(client);
  const value = await getAsync(itemId);
  return value;
};

app.get('/list_products', (req, res) => {
  const modifiedProductList = listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    intialAvailableQuantity: item.stock,
  }));
  res.setHeader('Content-Type', 'application/json');
  res.json(modifiedProductList);
});

app.get('/list_products/:itemId', (req, res) => {
  const { itemId } = req.params;
  try {
    getCurrentReservedStockById(itemId).then((value) => {
      if (!value) {
        res.statusCode = 404;
        return res.json({ status: 'Product not found' });
      } else {
        return res.json(JSON.parse(value));
      }
    });
  } catch (error) {
    res.statusCode = 500;
    res.json({ status: 'Internal Server Error' });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemByid(parseInt(itemId));
  if (!item) {
    res.statusCode = 404;
    return res.json({ status: 'Product not found' });
  }
  if (item['stock'] < 1) {
    return res.json({ status: 'Not enough stock available', itemId: itemId });
  }
  reserveStockById(itemId, item);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

module.exports = app;
