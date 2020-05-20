<h1 align="center">Звіт до лабораторної роботи №5</h1>

<h2 align="center">Виконання роботи</h2>
<strong>Варіант №4</strong>
<br />
Дано: <br />
<strong>
  i = 2,
  j = 6
</strong>
<hr />
<img src="https://github.com/RostyslavBoretskiy/TR31-TOTM2020/blob/master/LAB5/002.jpg" />
Теорема про пропускну здатність та максимальний потік
<br />
Можливе снування двох потоків
<br />
<hr />
Побудувати маршрут для:
<br />
С(1-4)=1000 Мбіт/с
<br />
С(2-4)=2500 Мбіт/с
<br />
С(1-5)=1500 Мбіт/с
<br />


<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Маршрут</th>
    <th class="tg-0lax">1-2</th>
    <th class="tg-0lax">1-3</th>
    <th class="tg-0lax">1-6</th>
    <th class="tg-0lax">2-3</th>
    <th class="tg-0lax">2-5</th>
    <th class="tg-0lax">3-4</th>
    <th class="tg-0lax">3-5</th>
    <th class="tg-0lax">3-6</th>
    <th class="tg-0lax">4-5</th>
    <th class="tg-0lax">Мбіт/с</th>
    <th class="tg-0lax">Мбіт/с</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">1-3-4</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1000</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1000</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1000</td>
    <td class="tg-0lax">1000</td>
  </tr>
  <tr>
    <td class="tg-0lax">2-5-4</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">800</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">800</td>
    <td class="tg-0lax">800</td>
    <td class="tg-0lax">2600</td>
  </tr>
  <tr>
    <td class="tg-0lax">2-3-4</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">800</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">800</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">800</td>
    <td class="tg-0lax">2600</td>
  </tr>
  <tr>
    <td class="tg-0lax">2-1-3-4</td>
    <td class="tg-0lax">400</td>
    <td class="tg-0lax">400</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">400</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">400</td>
    <td class="tg-0lax">2600</td>
  </tr>
  <tr>
    <td class="tg-0lax">2-3-5-4</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax">2600</td>
  </tr>
  <tr>
    <td class="tg-0lax">1-3-5</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1000</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1000</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1000</td>
    <td class="tg-0lax">1600</td>
  </tr>
  <tr>
    <td class="tg-0lax">1-3-5</td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax">600</td>
    <td class="tg-0lax">1600</td>
  </tr>
</tbody>
</table>


<strong>Висновок:</strong> в результаті лабораторної роботи ми дослідили можливе існування двох потоків. Для першого рівне 1000 Мбіт/с, для другого- 2600 Мбіт/с, а для третього- 1600 Мбіт/с.

