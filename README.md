# TwitterBot

MagicEden Marketplace Latest Sale Bot:
Note: Encrypted config file values using Fernet to protect Twitter bot access.

1) Application scrapes MagicEden marketplace for latest sale.
2) Once sale is retrieved, the NFT number and sale price is taken. $SOL sale price is converted into USD using latest $SOL price.
3) Using tweepy, Twitter bot posts the sale and information. 

Things to add:
- image of NFT in posts and transaction details (seller address and buyer address) 
- host on server to run automatically
- find a way to not use web scraper (monitor candy machine activity instead)
