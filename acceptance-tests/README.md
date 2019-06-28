## Setup:
* Run Fitnesse server:
```
java -jar fitnesse-standalone.jar -p 8080
```

* Open browser on `localhost:8080`

* Update paths in wiki test pages to match this directory:

```
!define TEST_SYSTEM {slim}
!define COMMAND_PATTERN {SlimJS %p}
!define COMMAND_PATTERN {node C:\Users\Bartek\studia\fitnesse-node\node_modules\slimjs\src\SlimJS %p}
!define SLIM_PORT {9086}
!path C:\Users\Bartek\studia\fitnesse-node
```
