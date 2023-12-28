from bs4 import BeautifulSoup
import re

def append_values_to_heading(soup):
    for root_selection in soup.find_all(class_='rootselection'):
        # Find the h4 tag
        heading = root_selection.find('h4')
        if heading:
            print(f"Processing: {heading.text}")

            # Extract the relevant part from the h4 text
            h4_text_part = re.split(r" \[", heading.text)[0]

            # Search for the corresponding table row
            for table in root_selection.find_all('table'):
                trs = table.find_all('tr')
                for tr in trs:
                    tds = tr.find_all('td')
                    if len(tds) > 1 and h4_text_part in tds[0].text:
                        # Extract relevant values from tds
                        values = [td.text.strip() for td in tds[1:7]]
                        if len(values) >= 6:
                            values_text = ' - M {} T {} SV {} W {} LD {} OC {}'.format(*values)
                            heading.string = f"{heading.text} {values_text}"
                            print(f"Updated: {heading}")
                            break


def add_minimize_functionality(soup):
    # Iterate through each rootselection and wrap its contents except the heading
    for root_selection in soup.find_all(class_='rootselection'):
        # Create a new div to hold the contents that need to be toggled
        content_div = soup.new_tag('div', attrs={'class': 'toggle-content'})

        # Move everything except the first h4 (the heading) into this div
        elements_to_move = root_selection.find_all(recursive=False)[1:]  # all elements after the first (h4)
        for element in elements_to_move:
            content_div.append(element.extract())  # move each element into content_div

        # Insert content_div back into root_selection
        root_selection.append(content_div)

    # Add CSS to hide toggle-content by default
    style_tag = soup.new_tag("style")
    style_tag.string = """
    .toggle-content { display: none; }
    .rootselection > h4 { cursor: pointer; }
    """
    soup.head.append(style_tag)

    # Add JavaScript to handle the toggle functionality
    script_tag = soup.new_tag("script")
    script_tag.string = """
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('.rootselection > h4').forEach(function(heading) {
            heading.addEventListener('click', function() {
                var contentDiv = this.nextElementSibling;
                contentDiv.style.display = contentDiv.style.display === 'none' ? 'block' : 'none';
            });
        });
    });
    """
    soup.body.append(script_tag)

def reformat_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    append_values_to_heading(soup)
    add_minimize_functionality(soup)
    formatted_content = soup.prettify()

    new_file_name = file_path.rsplit('.', 1)[0] + '_reformatted.html'
    with open(new_file_name, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"File reformatted and saved as '{new_file_name}'")

def main():
    file_path = input("Enter the path to the HTML file: ")
    reformat_html(file_path)

if __name__ == "__main__":
    main()