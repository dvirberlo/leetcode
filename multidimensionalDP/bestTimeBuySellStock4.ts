// function maxProfit(k: number, prices: number[]): number {
//   const n = prices.length;
//   function f(i: number, t: number): number {
//     if (i <= 0 || t === 0) return 0;
//     let result = -Infinity;
//     for (let j = 0; j < i; j++) {
//       result = Math.max(result, -prices[j] + f(j - 1, t - 1));
//     }
//     return Math.max(0, prices[i] + result, f(i - 1, t));
//   }
//   return f(n - 1, k);
// }

function maxProfit(prices: number[]): number {
  let minBuy1 = prices[0];
  let maxProfit1 = 0;
  let minBuy2 = prices[0] - maxProfit1;
  let maxProfit2 = 0;
  for (let i = 1; i < prices.length; i++) {
    maxProfit2 = Math.max(maxProfit2, prices[i] - minBuy2);
    minBuy2 = Math.min(minBuy2, prices[i] - maxProfit1);

    maxProfit1 = Math.max(maxProfit1, prices[i] - minBuy1);
    minBuy1 = Math.min(minBuy1, prices[i]);
  }
  return maxProfit2;
}

function maxProfit(k: number, prices: number[]): number {
  const minBuy = Array(k).fill(prices[0]);
  const maxProfit = Array(k).fill(0);
  for (let i = 1; i < prices.length; i++) {
    for (let t = 0; t < k; t++) {
      maxProfit[t] = Math.max(maxProfit[t], prices[i] - minBuy[t]);
      minBuy[t] = Math.min(
        minBuy[t],
        prices[i] - (t > 0 ? maxProfit[t - 1] : 0)
      );
    }
  }
  return maxProfit[k - 1];
}
