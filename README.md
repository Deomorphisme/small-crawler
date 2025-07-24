# small-crawler

This repository, created by Deo Gracias Sekongo, contains a Python script for crawling web pages within a specific domain. The script allows you to retrieve all links from a webpage and recursively explore them to find all pages within the same domain. It also offers the option to filter links by a specific subdirectory.


## Features

- **Subdirectory Filtering**: Allows specifying a subdirectory to limit the search to that subdirectory.
- **Valid Link Filtering**: Ignores `mailto:` and `javascript:` links to retrieve only valid web pages.
- **Duplicate Removal**: Eliminates duplicate links to keep only unique results.
- **Alphabetical Sorting**: Sorts the found links in alphabetical order for better readability.
- **Display of Found Pages Count**: Shows the total number of pages found at the end of execution.

## Usage

To use this script, you need to have Python 3 installed on your machine. You can run the script using the following command line:


```bash
python small_crawler.py <url> [subdir]
```
Or

```bash
./small_crawler.py <url> [subdir]
```

- `<url>`: The URL of the webpage to analyze.
- `[subdir]`: (Optional) The subdirectory to crawl.

### Example

```bash
python script.py https://example.com subdir1
```

This will execute the script and display all links from the `subdir1` subdirectory of `example.com`, sorted in alphabetical order.

## Installation

1. Clone this repository to your local machine:


```bash
git clone https://github.com/your-username/web-crawler-script.git
```

2. Navigate to the project directory:


```bash
cd web-crawler-script
```

3. Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Contribution

Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
