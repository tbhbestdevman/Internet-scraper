```python
import json
from scrapy.exporters import JsonItemExporter
from .items import WebScraperItem

class WebScraperPipeline:
    def __init__(self):
        self.file = open("scraped_data.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, WebScraperItem):
            self.exporter.export_item(item)
        return item
```