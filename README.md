# cicd-workshop-highercloud

## Docker command

在Docker中，--link參數已經被棄用，取而代之的是使用自定義的網路（Custom Networks）或者Docker Compose來實現容器之間的連結。然而，如果您仍然需要使用--link參數，以下是一個示例來說明如何使用它：

假設您有一個名為my-python-app的容器需要連結到一個名為my-redis的Redis容器，您可以使用以下指令來啟動my-python-app容器並附加連結到my-redis容器：

```bash
docker run --name my-python-app --link my-redis:redis -d my-python-app-image
```

在這個指令中，`--link` 參數的語法為 `--link <container_name>:<alias>`，其中 `<container_name>` 是要連結的容器名稱，而 ` <alias>` 是在my-python-app容器內部使用的別名。這樣，my-python-app 容器就可以透過 redis 這個別名來連接到 my-redis 容器。

請注意，雖然 `--link` 參數仍然可以使用，但官方建議使用自定義的網路（Custom Networks）或者Docker Compose來取代--link參數，因為這些方法提供了更靈活和強大的容器連結功能。
