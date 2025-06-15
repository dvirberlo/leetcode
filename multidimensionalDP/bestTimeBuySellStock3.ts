// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   let result = oneTransaction(prices, 0, n);
//   for (let i = 1; i < n; i++) {
//     const left = oneTransaction(prices, 0, i);
//     const right = oneTransaction(prices, i, n);
//     result = Math.max(result, left + right);
//   }
//   return result;
// }

// function oneTransaction(prices: number[], start: number, stop: number): number {
//   if (stop - start <= 1) return 0;
//   let minPrice = prices[start],
//     maxProfit = 0;
//   for (let i = start + 1; i < stop; i++) {
//     minPrice = Math.min(minPrice, prices[i]);
//     maxProfit = Math.max(maxProfit, prices[i] - minPrice);
//   }
//   return maxProfit;
// }

// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   const minS = Array(n),
//     maxS = Array(n);
// //   const minE = Array(n),
// //     maxE = Array(n);
// //   minS[0] = maxS[0] = prices[0];
// //   minE[n - 1] = maxE[n - 1] = prices[n - 1];
//   for (let i = 1; i < n; i++) {
//     minS[i] = Math.min(minS[i - 1], prices[i]);
//     maxS[i] = Math.max(maxS[i - 1], prices[i] - minS[i]);

//     // const j = n - 1 - i;
//     // minE[j] = Math.min(minE[j + 1], prices[j]);
//     // maxE[j] = Math.max(maxE[j + 1], prices[j] - minE[j]);
//   }
// //   console.log(prices, minS, maxS, minE, maxE);
//   let result = 0;
//   let minPrice = prices[start],
//     maxProfit = 0;
//   for (let i = 0; i < n - 1; i++) {
//     const left = maxS[i] - minS[i];
//     const right = maxE[i + 1] - minE[i + 1];
//     result = Math.max(result, left + right);
//     console.log(`i: ${i}, left: ${left}, right: ${right}, result: ${result}`);
//   }
//   return result;
// }

// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   let result = oneTransaction(prices, 0, n);
//   for (let i = 1; i < n; i++) {
//     const left = oneTransaction(prices, 0, i);
//     const right = oneTransaction(prices, i, n);
//     result = Math.max(result, left + right);
//   }
//   return result;
// }

// function oneTransaction(prices: number[], start: number, stop: number): number {
//   if (stop - start <= 1) return 0;
//   const minPrices: number[] = Array(stop).fill(prices[start]);
//   for (let i = start + 1; i < stop; i++) {
//     minPrices[i] = Math.min(prices[i], minPrices[i-1]);
//   }
//   let maxProfit = 0;
//   for (let i = start + 1; i < stop; i++) {
//     maxProfit = Math.max(maxProfit, prices[i] - minPrices[i]);
//   }
//   return maxProfit;
// }

// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   function f(i: number, m: number, b: boolean): number {
//     if (i >= n) return 0;
//     if (!b) return Math.max(prices[i] - m, f(i + 1, Math.min(m, prices[i]), b));
//     return Math.max(
//       Math.max(prices[i] - m, f(i + 1, Math.min(m, prices[i]), b)),
//       Math.max(prices[i] - m, 0) + f(i + 1, Number.MAX_VALUE, false)
//     );
//   }
//   return f(0, Number.MAX_VALUE, true);
// }

// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   function f(i: number, mi: number, b: boolean): number {
//     if (i >= n) return 0;
//     const m = prices[mi] ?? Number.MAX_VALUE;
//     const newM = prices[i] < m ? i : mi;
//     if (!b) return Math.max(prices[i] - m, f(i + 1, newM, b));
//     return Math.max(
//       Math.max(prices[i] - m, f(i + 1, newM, b)),
//       Math.max(prices[i] - m, 0) + f(i + 1, n, false)
//     );
//   }
//   return f(0, n, true);
// }

// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   function f(i: number, t: number): number {
//     if (i <= 0 || t === 0) return 0;
//     let result = -Infinity;
//     for (let j = 0; j < i; j++) {
//       result = Math.max(result, -prices[j] + f(j - 1, t - 1));
//     }
//     return Math.max(0, prices[i] + result, f(i - 1, t));
//   }
//   return f(n - 1, 2);
// }

// function maxProfit(prices: number[]): number {
//   const n = prices.length;
//   const f_1 = Array(n).fill(0);
//   let minPrice = prices[0];
//   for (let i = 1; i < n; i++) {
//     minPrice = Math.min(minPrice, prices[i]);
//     f_1[i] = Math.max(f_1[i - 1], prices[i] - minPrice);
//   }
//   const pf_2 = Array(n).fill(-prices[0] + f_1[0]);
//   for (let i = 1; i < n; i++) {
//     pf_2[i] = Math.max(pf_2[i - 1], -prices[i] + f_1[i - 1]);
//   }
//   const f_2 = Array(n).fill(0);
//   for (let i = 1; i < n; i++) {
//     f_2[i] = Math.max(f_2[i - 1], prices[i] + pf_2[i - 1]);
//   }
//   return f_2[n - 1];
// }

function maxProfit(prices: number[]): number {
  const n = prices.length;
  let minPrice = prices[0];
  let f1i = 0;
  let pf2i = -prices[0] + f1i;
  let f2i = 0;
  for (let i = 1; i < n; i++) {
    f2i = Math.max(f2i, prices[i] + pf2i);

    pf2i = Math.max(pf2i, -prices[i] + f1i);

    minPrice = Math.min(minPrice, prices[i]);
    f1i = Math.max(f1i, prices[i] - minPrice);
  }
  return f2i;
}
