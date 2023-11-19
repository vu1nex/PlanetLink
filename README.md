# PlanetLink

A pypi package to send message in different mediums.

## Usage

1. **import**

   ```python
   from PlanetLink.wxBot import wxBot
   ```

2. **define veriables**

   ```python
   corpid = 'xxxxxxxxxx'
   corpsecret = 'xxxxxxxxxxxxxxxxxxxxxx'
   agentid = 'xxxxxx'
   title = 'title'
   sign = 'sign'
   ```

3. **initial**

   ```python
   bot = wxBot()
   bot.initBot(corpid,corpsecret,agentid,title,sign)
   ```

4. **add content to wxMessageDemo**
   ```python
   bot.addContent("title: 'test1'\nvalue: 'val1'")
   bot.addContent("title: 'test2'\nvalue: 'val2'")
   ```

5. **send**
   ```python
   bot.send()
   ```
   
6. **get message**

   ```
   Message: ⛔ title
   [2023-11-16 16:59:17]
   ========================
   title: 'test1'
   value: 'val1'
   -------------------------------------
   title: 'test2'
   value: 'val2'
   -------------------------------------
   ```

## Message Configs

### **Sign and symbol**

| **sign**     | **symbol** |
| ------------------ | ---------------- |
| WARNING  | ⚠️   |
| ERROR    | ❌     |
| COMPLETE | ✅     |
| INFO     | 🔵     |
| ELSE     | ⛔     |


## TODO List

* [x] ~~release pypi package~~
* [ ] add return value and error log
* [ ] add list form of message

## Update History

* [20220924] first version of weChat message send API
* [20231116] rebuild code and release the first pypi package

## Pypi release version log

- `0.0.1` : first version of PlanetLink
- `0.0.2` : add clearContent and getSendContent function
