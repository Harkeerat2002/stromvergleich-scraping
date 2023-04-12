# Instructions on Web-Scraping
## Running the Extension on your Browser
1. In order to get this project running you would need the following extension on your browser:
 **Web Scraper - Free Web Scraping**
2. After having installed the extension, open a new page using the keyboard shortcut **Ctrl + Shift + i** to open the "Inspect Element" Page.
3. In the Inspect Element Page, click on the **Web Scraper** tab.
4. Click on *Create new Sitemap* -> *Import Sitemap*.
5. Copy Paste the following in **Sitemap JSON** (make sure that it is one continous link with no spaces):

``` json
{"_id":"stromvergleich","startUrl":["https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=80331&campaignId=&resultPage=1&product=electricity&locationId=40134&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&benchmarkProviderId=&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false"],"selectors":[{"id":"product_wraper","multiple":true,"parentSelectors":["_root"],"selector":"li.js-tariff","type":"SelectorElement"},{"id":"name","multiple":false,"parentSelectors":["product_wraper"],"regex":"","selector":".js-rank2 a.provider-name","type":"SelectorText"},{"id":"price","multiple":false,"parentSelectors":["product_wraper"],"regex":"","selector":".js-rank2 a.end-price","type":"SelectorText"},{"id":"ct/kwh","multiple":false,"parentSelectors":["product_wraper"],"regex":"","selector":".js-rank2 .detailed b","type":"SelectorText"},{"id":"postal-code","multiple":false,"parentSelectors":["_root"],"regex":"\\b\\d{5}\\b","selector":"p.pretable-info","type":"SelectorText"},{"id":"vergleichspreis","multiple":false,"parentSelectors":["_root"],"regex":"\\d{1,3}(?:\\.\\d{3})*(?:,\\d{1,2})?\\s+Euro","selector":".pretable-info span","type":"SelectorText"}]}
```
6. Name the sitemap as you wish, in the instructions it will be referred to as "Sitemap stromvergleich".
7. Now click on *Sitemap stromvergleich* and then *Edit Metadata*.
8. Under **Start URL** add the URLs (with the plus button) which you want to scrap. The following URLs were previously used, but please ensure these are still up-to-date and encompass the wanted cities.
- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=14169
	
- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=80331&benchmarkProviderId=&campaignId=&resultPage=1&product=electricity&locationId=40134&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=20095&benchmarkProviderId=&campaignId=&resultPage=1&product=electricity&locationId=23132&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false
	
- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=49716&benchmarkProviderId=&campaignId=&resultPage=1&product=electricity&locationId=37601&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=50931

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=54568

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=78628&benchmarkProviderId=&campaignId=&resultPage=1&product=electricity&locationId=50160&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=09456&benchmarkProviderId=&campaignId=&resultPage=1&product=electricity&locationId=625&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=38100

- https://www.stromvergleich.de/stromrechner?priceGuaranteeMinDuration=12&maxContractDuration=12&maxTariffsPerProvider=4&profile=h0&consumption=3000&zip=34233&campaignId=&resultPage=1&product=electricity&locationId=21653&consumptionOffPeak=0&offPeakPercentage=0&heatingPower=31.25&prepayment=false&includeTariffsWithDeposit=false&includeNonCompliantTariffs=false&includePackageTariffs=false&includeOnlineTariffs=true&includeMinimumUsageTariffs=false&onlyProductsWithGoodCustomerRating=false&onlyEcoTariffs=false&bonusIncluded=compliant&signupOnly=true&maxResultsPerPage=50&benchmarkTariffId=0&benchmarkProviderId=&maxContractProlongation=0&cancellationPeriod=6&meterType=&presetAll=false&presetWarentest=false

10. After all the URLs have been added, click on *Site Map stromvergleich* then *Scrape* and then **Start Scraping**
11. Click on the refresh button in the inspect element.
12. Now click on *Sitemamp stromvergleich*, *Export Data* and then click on **.XLSX**.
13. Alternatively, you can save the document as a **.CSV** and use the python code to clean the data. This is not advised.
14. If you have choosen to follow step 12 instead of step 11, save the CSV in input directory to change the structure of that data. Follow the next steps to run the python script for the **.CSV**.

## Running the Python Script [Not Necessary]
### Dependencies
1. Python 3.6
2. Pandas
3. OS
### Instructions
1. Open the terminal and go to the directory where the python script is located.
2. Run the following command:
```bash
python3 main.py
```
3. The output will be in the output directory.
