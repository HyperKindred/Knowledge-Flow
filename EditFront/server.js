import express from 'express';
import history from 'connect-history-api-fallback';

const app = express();

// 使用 history 中间件
app.use(history());

// 设置静态文件目录
app.use(express.static('./dist'));

const port = 7777;
const host = '0.0.0.0';

app.listen(port, host, function (err) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`Server is running at http://${host}:${port}`);
});
