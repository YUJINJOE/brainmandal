s = """<tbody id="mandal-tbody">
                <tr>
                    <td>a1</td>
                    <td>a2</td>
                    <td>a3</td>
                    <td class="near">a4</td>
                    <td class="near">a5</td>
                    <td class="near">a6</td>
                    <td>a7</td>
                    <td>a8</td>
                    <td>a9</td>
                <tr>
                    <td>b1</td>
                    <td>b2</td>
                    <td>b3</td>
                    <td>b4</td>
                    <td class="topic">b5</td>
                    <td>b6</td>
                    <td>b7</td>
                    <td>b8</td>
                    <td>b9</td>
                <tr>
                    <td>c1</td>
                    <td>c2</td>
                    <td>c3</td>
                    <td>c4</td>
                    <td>c5</td>
                    <td>c6</td>
                    <td>c7</td>
                    <td>c8</td>
                    <td>c9</td>"""

lines = s.splitlines()
count = 0
for line in lines:
    line.replace('>')