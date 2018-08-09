'use strict';
const RippleAPI = require('ripple-lib').RippleAPI;

const api = new RippleAPI({
  server: 'wss://s1.ripple.com' // Public rippled server
});
api.connect().then(() => {
  return api.generateAddress();
}).then(info => {
  console.log(info);
}).then(() => {
  return api.disconnect();
});

// 'use strict';
// const RippleAPI = require('ripple-lib').RippleAPI;

// const api = new RippleAPI({
//   server: 'wss://s1.ripple.com' // Public rippled server
// });
// api.connect().then(() => {
//   var address= api.generateAddress();
//   api.disconnect();
//   console
//   return address;
// });