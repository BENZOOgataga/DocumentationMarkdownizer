# Pterodactyl v1 API Reference

Welcome to the Pterodactyl v1 API documentation. This documentation is unofficial and provided by Dashflo.

If you find any errors throughout this API reference, please [let us know](https://dashflo.net/tickets/new). A special thanks to everyone who has helped contribute!

**The legacy Pterodactyl v0.7 API documentation[can be found here](https://dashflo.net/docs/api/pterodactyl/v0.7/).** Please remember you should not be using v0.7, and should upgrade as soon as possible.

Pterodactyl Links: **[Website](https://pterodactyl.io/)** | **[GitHub](https://github.com/pterodactyl)** | **[Discord](https://discord.gg/pterodactyl)**

# Authentication

A user can generate an client API key from: <https://pterodactyl.app/account/api> An admin can generate an application API key from: <https://pterodactyl.app/admin/api>

API keys are entered as bearer tokens with all API requests. Here is an example CURL request:

    curl "<endpoint>"
      -H "Authorization: Bearer <API-Key>"
      -H "Content-Type: application/json" \
      -H "Accept: Application/vnd.pterodactyl.v1+json" \

# Ratelimits

240 requests can be made each minute. Headers are returned to show thelimit, and how many are used within minute.

    x-ratelimit-limit: 240
    x-ratelimit-remaining: 237

# Docs Guide

Some API routes require data input, or have additional information that can be provided. The route will include table(s) with the available parameters.

Name | Description
---|---
Include parameters | List of parameters that can be used after adding `?include=<parameters>,<more-parameters>` to the route
Available parameters | List of all the different parameters available such as `?example=something&example2=something`
Filters | Filter the data to only include certain information `?filter[uuid]=something`
Sort by | Sort the returned results `?sort=-id`. Add a `-` before the sort type to reverse the order
Fields | Data input fields

You can combine multiple filters, it'll look for all matching results. For example, you could add &filter[uuid]=3387 and then it'll only return test@example.com.

* * *

[![Dashflo](https://cdn.dashflo.net/promotions/banners/service/minecraft/7u54t2qnuu8qTRv4.png?cache300620192021)](https://dashflo.net/store/dedicated-servers)

cURL

## [ /api/client ] Client

* * *

### **GET** [ / ] List servers

    https://pterodactyl.file.properties/api/client

Lists all servers

## Include parameters

Parameter | Description
---|---
egg | Information about the egg the server uses
subusers | List of subusers on the server

Headers

Accept

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client" \
      -H 'Accept: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "server",
          "attributes": {
            "server_owner": true,
            "identifier": "1a7ce997",
            "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "name": "Gaming",
            "node": "Test",
            "sftp_details": {
              "ip": "pterodactyl.file.properties",
              "port": 2022
            },
            "description": "Matt from Wii Sports",
            "limits": {
              "memory": 512,
              "swap": 0,
              "disk": 200,
              "io": 500,
              "cpu": 0
            },
            "feature_limits": {
              "databases": 5,
              "allocations": 5,
              "backups": 2
            },
            "is_suspended": false,
            "is_installing": false,
            "relationships": {
              "allocations": {
                "object": "list",
                "data": [
                  {
                    "object": "allocation",
                    "attributes": {
                      "id": 1,
                      "ip": "45.86.168.218",
                      "ip_alias": null,
                      "port": 25565,
                      "notes": null,
                      "is_default": true
                    }
                  },
                  {
                    "object": "allocation",
                    "attributes": {
                      "id": 2,
                      "ip": "45.86.168.218",
                      "ip_alias": null,
                      "port": 25566,
                      "notes": "Votifier",
                      "is_default": false
                    }
                  }
                ]
              }
            }
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 1,
          "count": 1,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **GET** [ /permissions ] Show permissions

    https://pterodactyl.file.properties/api/client/permissions

Retries all available permissions

This is used for the frontend

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/permissions" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "system_permissions",
      "attributes": {
        "permissions": {
          "websocket": {
            "description": "Allows the user to connect to the server websocket, giving them access to view console output and realtime server stats.",
            "keys": {
              "connect": "Allows a user to connect to the websocket instance for a server to stream the console."
            }
          },
          "control": {
            "description": "Permissions that control a user's ability to control the power state of a server, or send commands.",
            "keys": {
              "console": "Allows a user to send commands to the server instance via the console.",
              "start": "Allows a user to start the server if it is stopped.",
              "stop": "Allows a user to stop a server if it is running.",
              "restart": "Allows a user to perform a server restart. This allows them to start the server if it is offline, but not put the server in a completely stopped state."
            }
          },
          "user": {
            "description": "Permissions that allow a user to manage other subusers on a server. They will never be able to edit their own account, or assign permissions they do not have themselves.",
            "keys": {
              "create": "Allows a user to create new subusers for the server.",
              "read": "Allows the user to view subusers and their permissions for the server.",
              "update": "Allows a user to modify other subusers.",
              "delete": "Allows a user to delete a subuser from the server."
            }
          },
          "file": {
            "description": "Permissions that control a user's ability to modify the filesystem for this server.",
            "keys": {
              "create": "Allows a user to create additional files and folders via the Panel or direct upload.",
              "read": "Allows a user to view the contents of a directory and read the contents of a file. Users with this permission can also download files.",
              "update": "Allows a user to update the contents of an existing file or directory.",
              "delete": "Allows a user to delete files or directories.",
              "archive": "Allows a user to archive the contents of a directory as well as decompress existing archives on the system.",
              "sftp": "Allows a user to connect to SFTP and manage server files using the other assigned file permissions."
            }
          },
          "backup": {
            "description": "Permissions that control a user's ability to generate and manage server backups.",
            "keys": {
              "create": "Allows a user to create new backups for this server.",
              "read": "Allows a user to view all backups that exist for this server.",
              "update": "",
              "delete": "Allows a user to remove backups from the system.",
              "download": "Allows a user to download backups."
            }
          },
          "allocation": {
            "description": "Permissions that control a user's ability to modify the port allocations for this server.",
            "keys": {
              "read": "Allows a user to view the allocations assigned to this server.",
              "create": "Allows a user to assign additional allocations to the server.",
              "update": "Allows a user to change the primary server allocation and attach notes to each allocation.",
              "delete": "Allows a user to delete an allocation from the server."
            }
          },
          "startup": {
            "description": "Permissions that control a user's ability to view this server's startup parameters.",
            "keys": {
              "read": "",
              "update": ""
            }
          },
          "database": {
            "description": "Permissions that control a user's access to the database management for this server.",
            "keys": {
              "create": "Allows a user to create a new database for this server.",
              "read": "Allows a user to view the database associated with this server.",
              "update": "Allows a user to rotate the password on a database instance. If the user does not have the view_password permission they will not see the updated password.",
              "delete": "Allows a user to remove a database instance from this server.",
              "view_password": "Allows a user to view the password associated with a database instance for this server."
            }
          },
          "schedule": {
            "description": "Permissions that control a user's access to the schedule management for this server.",
            "keys": {
              "create": "",
              "read": "",
              "update": "",
              "delete": ""
            }
          },
          "settings": {
            "description": "Permissions that control a user's access to the settings for this server.",
            "keys": {
              "rename": "",
              "reinstall": ""
            }
          }
        }
      }
    }

## [ /account ] Account

* * *

### **GET** [ / ] Account details

    https://pterodactyl.file.properties/api/client/account

Retrieves information about the account

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "user",
      "attributes": {
        "id": 1,
        "admin": true,
        "username": "admin",
        "email": "example@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "language": "en"
      }
    }

### **GET** [ /two-factor ] 2FA details

    https://pterodactyl.file.properties/api/client/account/two-factor

Generates a TOTP QR code image to allow the setup of 2FA

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/two-factor" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "data": {
        "image_url_data": "otpauth:\/\/totp\/Pterodactyl:example%40example.com?secret=LGYOWJEGVRPPGPWATP5ZHOYC7DHAYQ6S&issuer=Pterodactyl"
      }
    }

### **POST** [ /two-factor ] Enable 2FA

    https://pterodactyl.file.properties/api/client/account/two-factor

Enables TOTP 2FA using the QR code generated by the GET request

Uses code generated from `GET /account/two-factor`

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
code | required | string | TOTP Code |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "code": "505134"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/two-factor" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "code": "505134"
    }'

Example response - 200:

    {
      "object": "recovery_tokens",
      "attributes": {
        "tokens": [
          "MpBjHH8O08",
          "D9H0hktN6L",
          "ho8KiUpeV8",
          "06vZEfrYPf",
          "nFRySZ2ryh",
          "7K1cTrhGoV",
          "n6xpwwlJfv",
          "hAmyCsZxYO",
          "5FiMKFyNpH",
          "IViSFoRFvW"
        ]
      }
    }

Example response - 400:

    {
      "errors": [
        {
          "code": "TwoFactorAuthenticationTokenInvalid",
          "status": "400",
          "detail": "The token provided is not valid."
        }
      ]
    }

### **DELETE** [ /two-factor ] Disable 2FA

    https://pterodactyl.file.properties/api/client/account/two-factor

Disables TOTP 2FA on the account

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
password | required | string | Existing password |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "password": "password"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/two-factor" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "password": "password"
    }'

Example response - 204:

    // Successful

Example response - 400:

    // Incorrect password
    {
      "errors": [
        {
          "code": "BadRequestHttpException",
          "status": "400",
          "detail": "An error was encountered while processing this request."
        }
      ]
    }

### **PUT** [ /email ] Update email

    https://pterodactyl.file.properties/api/client/account/email

Updates the email address of the account

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
email | required | string | New email |
password | required | string | Existing password |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "email": "example@xample.com",
      "password": "Password"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/email" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PUT \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "email": "example@xample.com",
      "password": "Password"
    }'

Example response - 201:

    // Successful

Example response - 400:

    // Invalid email format
    {
      "errors": [
        {
          "code": "email",
          "detail": "The email must be a valid email address.",
          "source": {
            "field": "email"
          }
        }
      ]
    }

Example response - 400:

    // Invalid password
    {
      "errors": [
        {
          "code": "InvalidPasswordProvidedException",
          "status": "400",
          "detail": "The password provided was invalid for this account."
        }
      ]
    }

### **PUT** [ /password ] Update password

    https://pterodactyl.file.properties/api/client/account/password

Updates the password of the account

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
current_password | required | string | Existing password |
password | required | string | New password |
password_confirmation | required | string | Confirm new password |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "current_password": "Password",
      "password": "password",
      "password_confirmation": "password"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/password" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PUT \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "current_password": "Password",
      "password": "password",
      "password_confirmation": "password"
    }'

Example response - 204:

    // Successful

### **GET** [ /api-keys ] List API keys

    https://pterodactyl.file.properties/api/client/account/api-keys

Retries a list of API keys

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/api-keys" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "api_key",
          "attributes": {
            "identifier": "wwQ5DJ6X1XaFznQS",
            "description": "API Docs",
            "allowed_ips": [],
            "last_used_at": "2020-06-03T15:04:47+01:00",
            "created_at": "2020-05-18T00:12:43+01:00"
          }
        }
      ]
    }

### **POST** [ /api-keys ] Create API key

    https://pterodactyl.file.properties/api/client/account/api-keys

Generates a new API key

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
description | required | string | Note for the API key |
allowed_ips |  | object | List of allowed IPs |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "description": "Restricted IPs",
      "allowed_ips": [
        "127.0.0.1",
        "192.168.0.1"
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/api-keys" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "description": "Restricted IPs",
      "allowed_ips": ["127.0.0.1", "192.168.0.1"]
    }'

Example response - 201:

    {
      "object": "api_key",
      "attributes": {
        "identifier": "yjAZbHMyKrv9YRZ0",
        "description": "Restricted IPs",
        "allowed_ips": [
          "127.0.0.1",
          "192.168.0.1"
        ],
        "last_used_at": null,
        "created_at": "2020-08-17T04:44:42+01:00"
      },
      "meta": {
        "secret_token": "wiHiMbmgjLOkA2fPzRD6KdMe7Q9Cqaka"
      }
    }

### **DELETE** [ /api-keys/{identifier} ] Delete API key

    https://pterodactyl.file.properties/api/client/account/api-keys/NWKMYMT2Mrav0Iq2

Deletes the specified API key

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/account/api-keys/NWKMYMT2Mrav0Iq2" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

Example response - 404:

    // Non existing API key
    {
      "errors": [
        {
          "code": "NotFoundHttpException",
          "status": "404",
          "detail": "An error was encountered while processing this request."
        }
      ]
    }

## [ /servers/{server} ] Server

* * *

### **GET** [ / ] Server details

    https://pterodactyl.file.properties/api/client/servers/1a7ce997

Retrieves information about the specified server

## Include parameters

Parameter | Description
---|---
egg | Information about the egg the server uses
subusers | List of subusers on the server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "server",
      "attributes": {
        "server_owner": true,
        "identifier": "1a7ce997",
        "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
        "name": "Wuhu Island",
        "node": "Test",
        "sftp_details": {
          "ip": "pterodactyl.file.properties",
          "port": 2022
        },
        "description": "Matt from Wii Sports",
        "limits": {
          "memory": 512,
          "swap": 0,
          "disk": 200,
          "io": 500,
          "cpu": 0
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 5,
          "backups": 2
        },
        "is_suspended": false,
        "is_installing": false,
        "relationships": {
          "allocations": {
            "object": "list",
            "data": [
              {
                "object": "allocation",
                "attributes": {
                  "id": 1,
                  "ip": "45.86.168.218",
                  "ip_alias": null,
                  "port": 25565,
                  "notes": null,
                  "is_default": true
                }
              },
              {
                "object": "allocation",
                "attributes": {
                  "id": 2,
                  "ip": "45.86.168.218",
                  "ip_alias": null,
                  "port": 25566,
                  "notes": "Votifier",
                  "is_default": false
                }
              }
            ]
          }
        }
      },
      "meta": {
        "is_server_owner": true,
        "user_permissions": [
          "*",
          "admin.websocket.errors",
          "admin.websocket.install"
        ]
      }
    }

### **GET** [ /websocket ] Console details

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/websocket

Generates credentials to establish a websocket

## How to connect

  1. Connect to the websocket address (in this example "wss://pterodactyl.file.properties:8080/api/servers/1a7ce997-259b-452e-8b4e-cecc464142ca/ws")
  2. Send the token to the websocket like this: `{"event":"auth","args":["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6Ij..."]}`

  * Tokens last about 10-15 minutes, and the websocket will notify you once you need to send a new token with `{"event":"token expiring"}` and `{"event":"token expired"}`

## Things you can send

  * `{"event":"auth","args":["<token>"]}` # Authenticate with websocket
  * `{"event":"send stats","args":[null]}` # Request stats
  * `{"event":"send logs","args":[null]}` # Request logs
  * `{"event":"set state","args":["<power-action>"]}` # Send power action
  * `{"event":"send command","args":["<command>"]}` # Send command

## Things you'll receive

  * `{"event":"auth success"}` # Upon successful websocket authentication
  * `{"event":"status","args":["offline"]}` # Status updates of the server
  * `{"event":"console output","args":["[14:07:12] [Query Listener #1/INFO]: Query running on 0.0.0.0:25565"]}` # Logs from server
  * `{"event":"stats","args":["{\"memory_bytes\":526626816,\"memory_limit_bytes\":588800000,\"cpu_absolute\":588.815,\"network\":{\"rx_bytes\":1126,\"tx_bytes\":1126},\"state\":\"stopping\",\"disk_bytes\":128118626}"]}` # Stats from server
  * `{"event":"token expiring"}` # Token is expiring soon so request a new one and send it to the websocket
  * `{"event":"token expired"}` # Token has expired

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/websocket" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "data": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6Ij...",
        "socket": "wss:\/\/pterodactyl.file.properties:8080\/api\/servers\/1a7ce997-259b-452e-8b4e-cecc464142ca\/ws"
      }
    }

### **GET** [ /resources ] Resource usage

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/resources

Retrieves resource utilization of the specified server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/resources" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "stats",
      "attributes": {
        "current_state": "starting",
        "is_suspended": false,
        "resources": {
          "memory_bytes": 588701696,
          "cpu_absolute": 0,
          "disk_bytes": 130156361,
          "network_rx_bytes": 694220,
          "network_tx_bytes": 337090
        }
      }
    }

### **POST** [ /command ] Send command

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/command

Sends a command to the server

The server must be online to send a command to it. You will get HTTP 502 is the server if not online.

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
command | required | string | Command to send |

// Server offline { "errors": [ { "code": "HttpException", "status": "502", "detail": "An error was encountered while processing this request." } ] }

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "command": "say CodeCo says Hi!"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/command" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "command": "say CodeCo says Hi!"
    }'

Example response - 204:

    // Successful

### **POST** [ /power ] Change power state

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/power

Sends a power signal to the server

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
signal | required | string | Power signal to send |

## Signals

Signal | Description
---|---
start | Starts the server
stop | Gracefully stops the server
restart | Stops then starts the server
kill | Instantly end the server process

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "signal": "start"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/power" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "signal": "start"
    }'

Example response - 204:

    // Successful

## [ /databases ] Databases

* * *

### **GET** [ / ] List databases

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases

Lists all databases on a server

## Include parameters

Parameter | Description
---|---
password | Includes the database user password

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "server_database",
          "attributes": {
            "id": "bEY4yAD5",
            "host": {
              "address": "127.0.0.1",
              "port": 3306
            },
            "name": "s5_perms",
            "username": "u5_QsIAp1jhvS",
            "connections_from": "%",
            "max_connections": 0
          }
        },
        {
          "object": "server_database",
          "attributes": {
            "id": "E0A0Rw42",
            "host": {
              "address": "127.0.0.1",
              "port": 3306
            },
            "name": "s5_coreprotect",
            "username": "u5_2jtJx1nO1d",
            "connections_from": "%",
            "max_connections": 0
          }
        }
      ]
    }

### **POST** [ / ] Create database

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases

Creates a new database

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "database": "bans",
      "remote": "%"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "database": "bans",
      "remote": "%"
    }'

Example response - 200:

    {
      "object": "server_database",
      "attributes": {
        "id": "y9YVxO4V",
        "host": {
          "address": "127.0.0.1",
          "port": 3306
        },
        "name": "s5_punishments",
        "username": "u5_aeZqbGdCM9",
        "connections_from": "%",
        "max_connections": 0,
        "relationships": {
          "password": {
            "object": "database_password",
            "attributes": {
              "password": "=lR2orDOcwfKkM=BXb.BVF.C"
            }
          }
        }
      }
    }

### **POST** [ /{database}/rotate-password ] Rotate password

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases/bEY4yAD5/rotate-password

Changes the password of a specified database

Headers

Accept

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases/bEY4yAD5/rotate-password" \
      -H 'Accept: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "server_database",
      "attributes": {
        "id": "y9YVxO4V",
        "host": {
          "address": "127.0.0.1",
          "port": 3306
        },
        "name": "s5_punishments",
        "username": "u5_aeZqbGdCM9",
        "connections_from": "%",
        "max_connections": 0,
        "relationships": {
          "password": {
            "object": "database_password",
            "attributes": {
              "password": "vnFKXlJ.p77!EiGR+Kd3muB."
            }
          }
        }
      }
    }

### **DELETE** [ /{database} ] Delete database

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases/y9YVxO4V

Deletes the specified database

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/databases/y9YVxO4V" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /files ] File Manager

* * *

### **GET** [ /list ] List files

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/list?directory=%2Fcache

Lists all files of the server

## Available parameters

Parameter | Description
---|---
directory | URL encoded path to list files from

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/list?directory=%2Fcache" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "file_object",
          "attributes": {
            "name": "cache",
            "mode": "drwxr-xr-x",
            "size": 4096,
            "is_file": false,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "inode\/directory",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:20:36+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "logs",
            "mode": "drwxr-xr-x",
            "size": 4096,
            "is_file": false,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "inode\/directory",
            "created_at": "2020-07-13T12:42:02+00:00",
            "modified_at": "2020-07-13T12:42:02+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "plugins",
            "mode": "drwxr-xr-x",
            "size": 4096,
            "is_file": false,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "inode\/directory",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:07+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "world",
            "mode": "drwxr-xr-x",
            "size": 4096,
            "is_file": false,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "inode\/directory",
            "created_at": "2020-07-13T13:26:22+00:00",
            "modified_at": "2020-07-13T13:26:22+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "world_nether",
            "mode": "drwxr-xr-x",
            "size": 4096,
            "is_file": false,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "inode\/directory",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:15+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "world_the_end",
            "mode": "drwxr-xr-x",
            "size": 4096,
            "is_file": false,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "inode\/directory",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:15+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "whitelist.json",
            "mode": "-rw-r--r--",
            "size": 2,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "application\/json",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:07+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "version_history.json",
            "mode": "-rw-r--r--",
            "size": 46,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "application\/json",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:08+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "usercache.json",
            "mode": "-rw-r--r--",
            "size": 2,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "application\/json",
            "created_at": "2020-07-13T12:42:03+00:00",
            "modified_at": "2020-07-13T12:42:03+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "spigot.yml",
            "mode": "-rw-r--r--",
            "size": 3567,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2020-06-12T21:44:42+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "server.properties",
            "mode": "-rw-r--r--",
            "size": 955,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:59+00:00",
            "modified_at": "2020-07-13T12:41:59+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "server.jar",
            "mode": "-rw-r--r--",
            "size": 36175593,
            "is_file": true,
            "is_symlink": false,
            "is_editable": false,
            "mimetype": "application\/jar",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2020-06-12T22:38:46+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "permissions.yml",
            "mode": "-rw-r--r--",
            "size": 0,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "inode\/x-empty",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:08+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "paper.yml",
            "mode": "-rw-r--r--",
            "size": 5310,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2020-06-12T21:44:42+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "ops.json",
            "mode": "-rw-r--r--",
            "size": 2,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "application\/json",
            "created_at": "2020-07-13T12:42:03+00:00",
            "modified_at": "2020-07-13T12:42:03+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "hs_err_pid25.log",
            "mode": "-rw-r--r--",
            "size": 57099,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2020-06-12T20:36:55+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "help.yml",
            "mode": "-rw-r--r--",
            "size": 2576,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:21:07+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "eula.txt",
            "mode": "-rw-r--r--",
            "size": 250,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2019-12-25T05:20:57+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "commands.yml",
            "mode": "-rw-r--r--",
            "size": 598,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2020-06-12T21:44:36+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "bukkit.yml",
            "mode": "-rw-r--r--",
            "size": 1053,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "text\/plain",
            "created_at": "2020-07-13T12:41:55+00:00",
            "modified_at": "2020-06-12T21:44:36+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "banned-players.json",
            "mode": "-rw-r--r--",
            "size": 2,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "application\/json",
            "created_at": "2020-07-13T12:42:03+00:00",
            "modified_at": "2020-07-13T12:42:03+00:00"
          }
        },
        {
          "object": "file_object",
          "attributes": {
            "name": "banned-ips.json",
            "mode": "-rw-r--r--",
            "size": 2,
            "is_file": true,
            "is_symlink": false,
            "is_editable": true,
            "mimetype": "application\/json",
            "created_at": "2020-07-13T12:42:03+00:00",
            "modified_at": "2020-07-13T12:42:03+00:00"
          }
        }
      ]
    }

### **GET** [ /contents ] Get file contents

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/contents?file=%2Fpaper.yml

Displays the contents of the specified file

## Available parameters

Parameter | Description
---|---
file | URL encoded path to the desired file

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/contents?file=%2Fpaper.yml" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    # This is the main configuration file for Paper.
    # As you can see, there's tons to configure. Some options may impact gameplay, so use
    # with caution, and make sure you know what each option does before configuring.
    #
    # If you need help with the configuration or have any questions related to Paper,
    # join us in our Discord or IRC channel.
    #
    # Discord: https://paperdiscord.emc.gs
    # IRC: #paper @ irc.spi.gt ( http://irc.spi.gt/iris/?channels=paper )
    # Website: https://papermc.io/
    # Docs: https://paper.readthedocs.org/

    verbose: false
    config-version: 20
    settings:
      load-permissions-yml-before-plugins: true
      bungee-online-mode: true
      region-file-cache-size: 256
      incoming-packet-spam-threshold: 300
      save-player-data: true
      use-alternative-luck-formula: false
      suggest-player-names-when-null-tab-completions: true
      enable-player-collisions: true
      save-empty-scoreboard-teams: false
      velocity-support:
        enabled: false
        online-mode: false
        secret: ''
      async-chunks:
        enable: true
        load-threads: -1
      watchdog:
        early-warning-every: 5000
        early-warning-delay: 10000
      spam-limiter:
        tab-spam-increment: 1
        tab-spam-limit: 500
      book-size:
        page-max: 2560
        total-multiplier: 0.98
    messages:
      no-permission: '&cI''m sorry, but you do not have permission to perform this command.
        Please contact the server administrators if you believe that this is in error.'
      kick:
        authentication-servers-down: ''
        connection-throttle: Connection throttled! Please wait before reconnecting.
        flying-player: Flying is not enabled on this server
        flying-vehicle: Flying is not enabled on this server
    timings:
      enabled: true
      verbose: true
      server-name-privacy: false
      hidden-config-entries:
      - database
      - settings.bungeecord-addresses
      history-interval: 300
      history-length: 3600
      server-name: Unknown Server
    world-settings:
      default:
        per-player-mob-spawns: false
        optimize-explosions: false
        portal-search-radius: 128
        disable-teleportation-suffocation-check: false
        fixed-chunk-inhabited-time: -1
        use-vanilla-world-scoreboard-name-coloring: false
        remove-corrupt-tile-entities: false
        enable-treasure-maps: true
        treasure-maps-return-already-discovered: false
        experience-merge-max-value: -1
        prevent-moving-into-unloaded-chunks: false
        max-auto-save-chunks-per-tick: 24
        falling-block-height-nerf: 0
        tnt-entity-height-nerf: 0
        filter-nbt-data-from-spawn-eggs-and-related: true
        max-entity-collisions: 8
        disable-creeper-lingering-effect: false
        duplicate-uuid-resolver: saferegen
        duplicate-uuid-saferegen-delete-range: 32
        prevent-tnt-from-moving-in-water: false
        disable-thunder: false
        skeleton-horse-thunder-spawn-chance: 0.01
        disable-ice-and-snow: false
        count-all-mobs-for-spawning: false
        keep-spawn-loaded-range: 10
        keep-spawn-loaded: true
        auto-save-interval: -1
        armor-stands-do-collision-entity-lookups: true
        non-player-arrow-despawn-rate: -1
        creative-arrow-despawn-rate: -1
        nether-ceiling-void-damage-height: 0
        grass-spread-tick-rate: 1
        water-over-lava-flow-speed: 5
        bed-search-radius: 1
        fix-zero-tick-instant-grow-farms: true
        use-faster-eigencraft-redstone: false
        allow-non-player-entities-on-scoreboards: false
        disable-explosion-knockback: false
        container-update-tick-rate: 1
        parrots-are-unaffected-by-player-movement: false
        armor-stands-tick: true
        spawner-nerfed-mobs-should-jump: false
        entities-target-with-follow-range: false
        allow-leashing-undead-horse: false
        baby-zombie-movement-modifier: 0.5
        mob-spawner-tick-rate: 1
        all-chunks-are-slime-chunks: false
        game-mechanics:
          scan-for-legacy-ender-dragon: true
          disable-pillager-patrols: false
          disable-relative-projectile-velocity: false
          disable-chest-cat-detection: false
          shield-blocking-delay: 5
          disable-end-credits: false
          disable-player-crits: false
          disable-sprint-interruption-on-attack: false
          disable-unloaded-chunk-enderpearl-exploit: true
        max-growth-height:
          cactus: 3
          reeds: 3
        fishing-time-range:
          MinimumTicks: 100
          MaximumTicks: 600
        despawn-ranges:
          soft: 32
          hard: 128
        lightning-strike-distance-limit:
          sound: -1
          impact-sound: -1
          flash: -1
        frosted-ice:
          enabled: true
          delay:
            min: 20
            max: 40
        lootables:
          auto-replenish: false
          restrict-player-reloot: true
          reset-seed-on-fill: true
          max-refills: -1
          refresh-min: 12h
          refresh-max: 2d
        alt-item-despawn-rate:
          enabled: false
          items:
            COBBLESTONE: 300
        hopper:
          cooldown-when-full: true
          disable-move-event: false
        anti-xray:
          enabled: false
          engine-mode: 1
          chunk-edge-mode: 2
          max-chunk-section-index: 3
          update-radius: 2
          hidden-blocks:
          - gold_ore
          - iron_ore
          - coal_ore
          - lapis_ore
          - mossy_cobblestone
          - obsidian
          - chest
          - diamond_ore
          - redstone_ore
          - clay
          - emerald_ore
          - ender_chest
          replacement-blocks:
          - stone
          - oak_planks
        generator-settings:
          flat-bedrock: false
        squid-spawn-height:
          maximum: 0.0

### **GET** [ /download ] Download file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/download?file=%2Feula.txt

Generates a one-time link to download the specified file

## Available parameters

Parameter | Description
---|---
file | URL encoded path to the desired file

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/download?file=%2Feula.txt" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "signed_url",
      "attributes": {
        "url": "https:\/\/pterodactyl.file.properties:8080\/download\/file?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5NDY0ODEwMCwibmJmIjoxNTk0NjQ3ODAwLCJleHAiOjE1OTQ2NDkwMDAsImZpbGVfcGF0aCI6IlwvZXVsYS50eHQiLCJzZXJ2ZXJfdXVpZCI6IjFhN2NlOTk3LTI1OWItNDUyZS04YjRlLWNlY2M0NjQxNDJjYSIsInVuaXF1ZV9pZCI6IlNvWUdIamNaNmhKUVlieHUifQ.h4eBmxDXf-4GAwVuAWZFU5QTqd62jw7HTre4aKQGpvw"
      }
    }

### **PUT** [ /rename ] Rename file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/rename

Renames the specified file(s) or folder(s)

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "root": "/",
      "files": [
        {
          "from": "data",
          "to": "abc"
        }
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/rename" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PUT \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "root": "/",
      "files": [
        { "from": "data", "to": "abc"}
      ]
    }'

Example response - 204:

    // Successful

### **POST** [ /copy ] Copy file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/copy

Copies the specified file

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "location": "/server.properties"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/copy" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "location": "/server.properties"
    }'

Example response - 204:

    // Successful

### **POST** [ /write ] Write file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/write?file=%2Feula.txt

Writes data to the specified file

## Available parameters

Parameter | Description
---|---
file | URL encoded path to the desired file

Headers

Accept

application/json

Authorization

    Bearer apikey

Body raw

    #By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
    #You also agree that tacos are tasty, and the best food in the world.
    #Wed Dec 25 05:20:41 UTC 2019
    eula=true

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/write?file=%2Feula.txt" \
      -H 'Accept: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
    #You also agree that tacos are tasty, and the best food in the world.
    #Wed Dec 25 05:20:41 UTC 2019
    eula=true
    '

Example response - 204:

    // Successful

### **POST** [ /compress ] Compress file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/compress

Compresses the specified file

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "root": "/",
      "files": [
        "abc"
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/compress" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "root": "/",
      "files": [
        "abc"
      ]
    }'

Example response - 200:

    {
      "object": "file_object",
      "attributes": {
        "name": "archive-2020-08-23T220805Z.tar.gz",
        "mode": "-rw-------",
        "size": 0,
        "is_file": true,
        "is_symlink": false,
        "is_editable": false,
        "mimetype": "application\/tar+gzip",
        "created_at": "2020-08-23T22:08:05+00:00",
        "modified_at": "2020-08-23T22:08:05+00:00"
      }
    }

### **POST** [ /decompress ] Decompress file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/decompress

Decompresses the selected file

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "root": "/",
      "file": "archive-2020-08-23T220655Z.tar.gz"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/decompress" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "root": "/",
      "file": "archive-2020-08-23T220655Z.tar.gz"
    }'

Example response - 204:

    // Successful

### **POST** [ /delete] Delete file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/delete

Deletes the specified file(s) or folder(s)

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "root": "/maps",
      "files": [
        "worlds"
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/delete" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "root": "/maps",
      "files": [
        "worlds"
      ]
    }'

Example response - 204:

    // Successful

### **POST** [ /create-folder ] Create folder

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/create-folder

Creates the specified folder in the specified directory

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "root": "/maps",
      "name": "worlds"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/create-folder" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "root": "/maps",
      "name": "worlds"
    }'

Example response - 204:

    // Successful

### **GET** [ /upload ] Upload file

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/upload

Returns a signed URL used to upload files to the server using POST

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/files/upload" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "signed_url",
      "attributes": {
        "url": "https:\/\/pterodactyl.file.properties:8080\/upload\/file?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5ODIyMTMyMSwibmJmIjoxNTk4MjIxMDIxLCJleHAiOjE1OTgyMjIyMjEsInNlcnZlcl91dWlkIjoiMWE3Y2U5OTctMjU5Yi00NTJlLThiNGUtY2VjYzQ2NDE0MmNhIiwidW5pcXVlX2lkIjoiNmM2OFdkSkJTVzg0RlBsUiJ9.GJ5681K9ehhPCcXevyxw-RO1jhv4UWg5T8b_P7r6s8Q"
      }
    }

## [ /schedules ] Schedules

* * *

### **GET** [ / ] List schedules

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules

Lists all schedules added to the server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "server_schedule",
          "attributes": {
            "id": 1,
            "name": "Daily Reboot",
            "cron": {
              "day_of_week": "*",
              "day_of_month": "*",
              "hour": "0",
              "minute": "0"
            },
            "is_active": true,
            "is_processing": false,
            "last_run_at": null,
            "next_run_at": "2020-06-13T00:00:00+01:00",
            "created_at": "2020-06-12T23:50:14+01:00",
            "updated_at": "2020-06-12T23:53:07+01:00",
            "relationships": {
              "tasks": {
                "object": "list",
                "data": [
                  {
                    "object": "schedule_task",
                    "attributes": {
                      "id": 1,
                      "sequence_id": 1,
                      "action": "command",
                      "payload": "say Rebooting...",
                      "time_offset": 0,
                      "is_queued": false,
                      "created_at": "2020-06-12T23:50:46+01:00",
                      "updated_at": "2020-06-12T23:52:54+01:00"
                    }
                  },
                  {
                    "object": "schedule_task",
                    "attributes": {
                      "id": 2,
                      "sequence_id": 2,
                      "action": "power",
                      "payload": "restart",
                      "time_offset": 5,
                      "is_queued": false,
                      "created_at": "2020-06-12T23:53:07+01:00",
                      "updated_at": "2020-06-12T23:53:07+01:00"
                    }
                  }
                ]
              }
            }
          }
        }
      ]
    }

### **POST** [ / ] Create schedule

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules

Creates a new schedule

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
name | required | string | Friendly name for the schedule | min:1
is_active | optional | boolean | Specifies whether the schedule is active |
minute | required | string | Cron minute syntax |
hour | required | string | Cron hour syntax |
day_of_week | required | string | Cron day-of-month syntax |
day_of_month | required | string | Cron day-of-month syntax |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "Minute Hello",
      "minute": "*",
      "hour": "*",
      "day_of_month": "*",
      "day_of_week": "*",
      "is_active": true
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "Minute Hello",
      "minute": "*",
      "hour": "*",
      "day_of_month": "*",
      "day_of_week": "*",
      "is_active": true
    }'

Example response - 200:

    {
      "object": "server_schedule",
      "attributes": {
        "id": 4,
        "name": "Minute Hello",
        "cron": {
          "day_of_week": "*",
          "day_of_month": "*",
          "hour": "*",
          "minute": "*"
        },
        "is_active": true,
        "is_processing": false,
        "last_run_at": null,
        "next_run_at": "2020-06-13T15:17:00+01:00",
        "created_at": "2020-06-13T15:16:45+01:00",
        "updated_at": "2020-06-13T15:16:45+01:00",
        "relationships": {
          "tasks": {
            "object": "list",
            "data": []
          }
        }
      }
    }

### **GET** [ /{schedule} ] Schedule details

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/1

Retrieves specific schedule

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "server_schedule",
      "attributes": {
        "id": 1,
        "name": "Daily Reboot",
        "cron": {
          "day_of_week": "*",
          "day_of_month": "*",
          "hour": "0",
          "minute": "0"
        },
        "is_active": true,
        "is_processing": false,
        "last_run_at": null,
        "next_run_at": "2020-06-13T00:00:00+01:00",
        "created_at": "2020-06-12T23:50:14+01:00",
        "updated_at": "2020-06-12T23:53:07+01:00",
        "relationships": {
          "tasks": {
            "object": "list",
            "data": [
              {
                "object": "schedule_task",
                "attributes": {
                  "id": 1,
                  "sequence_id": 1,
                  "action": "command",
                  "payload": "say Rebooting...",
                  "time_offset": 0,
                  "is_queued": false,
                  "created_at": "2020-06-12T23:50:46+01:00",
                  "updated_at": "2020-06-12T23:52:54+01:00"
                }
              },
              {
                "object": "schedule_task",
                "attributes": {
                  "id": 2,
                  "sequence_id": 2,
                  "action": "power",
                  "payload": "restart",
                  "time_offset": 5,
                  "is_queued": false,
                  "created_at": "2020-06-12T23:53:07+01:00",
                  "updated_at": "2020-06-12T23:53:07+01:00"
                }
              }
            ]
          }
        }
      }
    }

### **POST** [ /{schedule} ] Update schedule

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/2

Updates the specified schedule

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
name | required | string | Friendly name for the schedule | min:1
is_active | optional | boolean | Specifies whether the schedule is active |
minute | required | string | Cron minute syntax |
hour | required | string | Cron hour syntax |
day _of_ week | required | string | Cron day-of-month syntax |
day _of_ month | required | string | Cron day-of-month syntax |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "Hourly Hello",
      "minute": "0",
      "hour": "*",
      "day_of_month": "*",
      "day_of_week": "*"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/2" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "Hourly Hello",
      "minute": "0",
      "hour": "*",
      "day_of_month": "*",
      "day_of_week": "*"
    }'

Example response - 200:

    {
      "object": "server_schedule",
      "attributes": {
        "id": 2,
        "name": "Hourly Hello",
        "cron": {
          "day_of_week": "*",
          "day_of_month": "*",
          "hour": "*",
          "minute": "0"
        },
        "is_active": false,
        "is_processing": false,
        "last_run_at": null,
        "next_run_at": "2020-06-13T16:00:00+01:00",
        "created_at": "2020-06-13T15:05:25+01:00",
        "updated_at": "2020-06-13T15:14:07+01:00",
        "relationships": {
          "tasks": {
            "object": "list",
            "data": []
          }
        }
      }
    }

### **DELETE** [ /{schedule} ] Delete schedule

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/2

Deletes the specified schedule

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/2" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

### **POST** [ /{schedule}/tasks ] Create task

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/7/tasks

Creates a new task on the specified schedule

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
action | required | string | Type of action to use |
payload | required | string | Payload to send |
time_offset | required | string | Offset in seconds |

# Actions

Action | Description
---|---
command | Sends power action
power | Changes power signal - Check power route for payloads
backup | Creates a backup

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "action": "command",
      "payload": "say Hello World",
      "time_offset": "0"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/7/tasks" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "action": "command",
      "payload": "say Hello World",
      "time_offset": "0"
    }'

Example response - 200:

    {
      "object": "schedule_task",
      "attributes": {
        "id": 6,
        "sequence_id": 1,
        "action": "command",
        "payload": "say Hello World",
        "time_offset": 0,
        "is_queued": false,
        "created_at": "2020-10-29T01:09:03+00:00",
        "updated_at": "2020-10-29T01:09:03+00:00"
      }
    }

### **POST** [ /{schedule}/tasks/{task} ] Update task

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/7/tasks/6

Updates the specified task

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
action | required | string | Type of action to use |
payload | required | string | Payload to send |
time_offset | required | string | Offset in seconds |

# Actions

Action | Description
---|---
command | Sends power action
power | Changes power signal - Check power route for payloads
backup | Creates a backup

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "action": "command",
      "payload": "say Updated Statement!?",
      "time_offset": "0"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/7/tasks/6" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "action": "command",
      "payload": "say Updated Statement!?",
      "time_offset": "0"
    }'

Example response - 200:

    {
      "object": "schedule_task",
      "attributes": {
        "id": 6,
        "sequence_id": 1,
        "action": "command",
        "payload": "say Updated Statement!?",
        "time_offset": 0,
        "is_queued": false,
        "created_at": "2020-10-29T01:09:03+00:00",
        "updated_at": "2020-10-29T01:10:30+00:00"
      }
    }

### **DELETE** [ /{schedule}/tasks/{task} ] Delete task

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/2/tasks/3

Deletes the specified task

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/schedules/2/tasks/3" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /network ] Network

* * *

### **GET** [ /allocations ] List allocations

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations

Retrieves the network information for the specified server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "allocation",
          "attributes": {
            "id": 1,
            "ip": "45.86.168.218",
            "ip_alias": null,
            "port": 25565,
            "notes": null,
            "is_default": true
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 2,
            "ip": "45.86.168.218",
            "ip_alias": null,
            "port": 25566,
            "notes": "Votifier",
            "is_default": false
          }
        }
      ]
    }

### **POST** [ /allocations ] Assign allocation

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations

Automatically assigns a new allocation if auto-assign is enabled on the instance

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "allocation",
      "attributes": {
        "id": 6,
        "ip": "45.86.168.218",
        "ip_alias": null,
        "port": 25570,
        "notes": null,
        "is_default": false
      }
    }

### **POST** [ /allocations/{allocation} ] Set allocation note

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations/2

Sets a note for the allocation

# Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
notes | required | string | Note for allocation |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "notes": "Votifier"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations/2" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "notes": "Votifier"
    }'

Example response - 200:

    {
      "object": "allocation",
      "attributes": {
        "id": 2,
        "ip": "45.86.168.218",
        "ip_alias": null,
        "port": 25566,
        "notes": "Votifier",
        "is_default": false
      }
    }

### **POST** [ /allocations/{allocation}/primary ] Set primary allocation

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations/1/primary

Sets the primary allocation

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations/1/primary" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "allocation",
      "attributes": {
        "id": 2,
        "ip": "45.86.168.218",
        "ip_alias": null,
        "port": 25566,
        "notes": "Votifier",
        "is_default": true
      }
    }

### **DELETE** [ /allocations/{allocation} ] Unassign allocation

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations/2

Deletes the specified non-primary allocation

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/network/allocations/2" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

Example response - 400:

    {
      "errors": [
        {
          "code": "DisplayException",
          "status": "400",
          "detail": "Cannot delete the primary allocation for a server."
        }
      ]
    }

## [ /users ] Users

* * *

### **GET** [ / ] List Users

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/users

Lists all users added to the server, along with details about them and their permissions

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/users" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "server_subuser",
          "attributes": {
            "uuid": "73f233ca-99e0-47a9-bd46-efd3296d7ad9",
            "username": "subuser1uxk",
            "email": "subuser1@example.com",
            "image": "https:\/\/gravatar.com\/avatar\/c0da5391b64449c1ecbfd4349184377c",
            "2fa_enabled": false,
            "created_at": "2020-06-12T23:18:43+01:00",
            "permissions": [
              "control.console",
              "control.start",
              "control.stop",
              "control.restart",
              "user.create",
              "user.update",
              "user.delete",
              "user.read",
              "file.create",
              "file.read",
              "file.update",
              "file.delete",
              "file.archive",
              "file.sftp",
              "backup.create",
              "backup.read",
              "backup.delete",
              "backup.update",
              "backup.download",
              "allocation.update",
              "startup.update",
              "startup.read",
              "database.create",
              "database.read",
              "database.update",
              "database.delete",
              "database.view_password",
              "schedule.create",
              "schedule.read",
              "schedule.update",
              "settings.rename",
              "schedule.delete",
              "settings.reinstall",
              "websocket.connect"
            ]
          }
        },
        {
          "object": "server_subuser",
          "attributes": {
            "uuid": "60a7aec3-e17d-4aa9-abb3-56d944d204b4",
            "username": "subuser2jvc",
            "email": "subuser2@example.com",
            "image": "https:\/\/gravatar.com\/avatar\/3bb1c751a8b3488f4a4c70eddfe898d8",
            "2fa_enabled": false,
            "created_at": "2020-06-12T23:31:41+01:00",
            "permissions": [
              "control.console",
              "control.start",
              "websocket.connect"
            ]
          }
        },
        {
          "object": "server_subuser",
          "attributes": {
            "uuid": "1287632d-9224-40c0-906e-f543423400bc",
            "username": "subuser3bvo",
            "email": "subuser3@example.com",
            "image": "https:\/\/gravatar.com\/avatar\/8b28d32aaa64a1564450d16f71a81f65",
            "2fa_enabled": false,
            "created_at": "2020-07-13T14:27:46+01:00",
            "permissions": [
              "control.console",
              "control.start",
              "websocket.connect"
            ]
          }
        },
        {
          "object": "server_subuser",
          "attributes": {
            "uuid": "2fcb6f7e-342a-423a-93a4-6111a237c0c7",
            "username": "geboc70057d6r",
            "email": "geboc70057@djemail.net",
            "image": "https:\/\/gravatar.com\/avatar\/354d25d88e2c73b9f8d8e9bb8f1bf15e",
            "2fa_enabled": false,
            "created_at": "2020-07-13T14:36:44+01:00",
            "permissions": [
              "control.console",
              "control.start",
              "websocket.connect"
            ]
          }
        },
        {
          "object": "server_subuser",
          "attributes": {
            "uuid": "b20e4e11-550f-4c52-893d-94fc8bc46a06",
            "username": "testidq",
            "email": "test@example.com",
            "image": "https:\/\/gravatar.com\/avatar\/55502f40dc8b7c769880b10874abc9d0",
            "2fa_enabled": false,
            "created_at": "2020-07-19T13:48:38+01:00",
            "permissions": [
              "control.*",
              "websocket.connect"
            ]
          }
        }
      ]
    }

### **POST** [ / ] Create User

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/users

Adds a user to the server

# Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
email | required | string | Email address of the user |
permissions | required | object | Permissions that user is permitted |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "email": "subuser2@example.com",
      "permissions": [
        "control.console",
        "control.start"
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/users" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "email": "subuser2@example.com",
      "permissions": [
        "control.console",
        "control.start"
      ]
    }'

Example response - 200:

    {
      "object": "server_subuser",
      "attributes": {
        "uuid": "60a7aec3-e17d-4aa9-abb3-56d944d204b4",
        "username": "subuser2jvc",
        "email": "subuser2@example.com",
        "image": "https:\/\/gravatar.com\/avatar\/3bb1c751a8b3488f4a4c70eddfe898d8",
        "2fa_enabled": false,
        "created_at": "2020-06-12T23:31:41+01:00",
        "permissions": [
          "control.console",
          "control.start",
          "websocket.connect"
        ]
      }
    }

### **GET** [ /{subuser} ] User details

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4

Retrieves information about a specific user

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "server_subuser",
      "attributes": {
        "uuid": "60a7aec3-e17d-4aa9-abb3-56d944d204b4",
        "username": "subuser2jvc",
        "email": "subuser2@example.com",
        "image": "https:\/\/gravatar.com\/avatar\/3bb1c751a8b3488f4a4c70eddfe898d8",
        "2fa_enabled": false,
        "created_at": "2020-06-12T23:31:41+01:00",
        "permissions": [
          "control.console",
          "control.start",
          "websocket.connect"
        ]
      }
    }

### **POST** [ /{subuser} ] Update user

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4

Updates the specified user

# Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
permissions | required | object | Permissions that user is permitted |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "permissions": [
        "control.console",
        "control.start"
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "permissions": [
        "control.console",
        "control.start"
      ]
    }'

Example response - 200:

    {
      "object": "server_subuser",
      "attributes": {
        "uuid": "60a7aec3-e17d-4aa9-abb3-56d944d204b4",
        "username": "subuser2jvc",
        "email": "subuser2@example.com",
        "image": "https:\/\/gravatar.com\/avatar\/3bb1c751a8b3488f4a4c70eddfe898d8",
        "2fa_enabled": false,
        "created_at": "2020-06-12T23:31:41+01:00",
        "permissions": [
          "control.console",
          "control.start",
          "websocket.connect"
        ]
      }
    }

### **DELETE** [ /{subuser} ] Delete user

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4

Removes the specified user from the server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /backups ] Backups

* * *

### **GET** [ / ] List backups

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups

Retrieves a list of backups

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "backup",
          "attributes": {
            "uuid": "904df120-a66f-4375-a4ae-40eedbeae630",
            "name": "Quick Backup",
            "ignored_files": [],
            "sha256_hash": "7c20d6a269b441a9dfd044e3f8ad13d77c09c83af8832d29ad603084a9a63726",
            "bytes": 114402862,
            "created_at": "2020-06-13T05:21:01+01:00",
            "completed_at": "2020-06-13T05:21:04+01:00"
          }
        },
        {
          "object": "backup",
          "attributes": {
            "uuid": "63087048-eada-419c-ad72-803c1c949cac",
            "name": "Backup at 2020-07-19 16:21:34",
            "ignored_files": [],
            "sha256_hash": "39bf93b9d8aee45316fa7ec8bbed0530904558851fa8e712452845c969873b16",
            "bytes": 114567250,
            "created_at": "2020-07-19T16:21:34+01:00",
            "completed_at": "2020-07-19T16:21:35+01:00"
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 2,
          "count": 2,
          "per_page": 20,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **POST** [ / ] Create backup

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups

Creates a new backup

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "backup",
      "attributes": {
        "uuid": "63087048-eada-419c-ad72-803c1c949cac",
        "name": "Backup at 2020-07-19 16:21:34",
        "ignored_files": [],
        "sha256_hash": null,
        "bytes": 0,
        "created_at": "2020-07-19T16:21:34+01:00",
        "completed_at": null
      }
    }

### **GET** [ /{backup} ] Backup details

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups/904df120-a66f-4375-a4ae-40eedbeae630

Retrieves information about the specified backup

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups/904df120-a66f-4375-a4ae-40eedbeae630" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "backup",
      "attributes": {
        "uuid": "904df120-a66f-4375-a4ae-40eedbeae630",
        "name": "Quick Backup",
        "ignored_files": [],
        "sha256_hash": "7c20d6a269b441a9dfd044e3f8ad13d77c09c83af8832d29ad603084a9a63726",
        "bytes": 114402862,
        "created_at": "2020-06-13T05:21:01+01:00",
        "completed_at": "2020-06-13T05:21:04+01:00"
      }
    }

### **GET** [ /{backup}/download ] Download backup

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups/904df120-a66f-4375-a4ae-40eedbeae630/download

Generates a download link for a backup

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups/904df120-a66f-4375-a4ae-40eedbeae630/download" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "signed_url",
      "attributes": {
        "url": "https:\/\/pterodactyl.file.properties:8080\/download\/backup?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5NTE3MjEyNSwibmJmIjoxNTk1MTcxODI1LCJleHAiOjE1OTUxNzMwMjUsImJhY2t1cF91dWlkIjoiOTA0ZGYxMjAtYTY2Zi00Mzc1LWE0YWUtNDBlZWRiZWFlNjMwIiwic2VydmVyX3V1aWQiOiIxYTdjZTk5Ny0yNTliLTQ1MmUtOGI0ZS1jZWNjNDY0MTQyY2EiLCJ1bmlxdWVfaWQiOiJKN1lIQUFUZzVoYVg4M1VOIn0.0zSozCFyjsYjGjUiPS76wM1WXX09FecNxdSZnj6rNt4"
      }
    }

### **DELETE** [ /{backup} ] Delete backup

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups/63087048-eada-419c-ad72-803c1c949cac

Deletes the specified backup

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/backups/63087048-eada-419c-ad72-803c1c949cac" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /startup ] Startup

* * *

### **GET** [ / ] List Variables

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/startup

Lists all variables on the server

Headers

Accept

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/startup" \
      -H 'Accept: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "egg_variable",
          "attributes": {
            "name": "Server Jar File",
            "description": "The name of the server jarfile to run the server with.",
            "env_variable": "SERVER_JARFILE",
            "default_value": "server.jar",
            "server_value": "server.jar",
            "is_editable": true,
            "rules": "required|regex:\/^([\\w\\d._-]+)(\\.jar)$\/"
          }
        },
        {
          "object": "egg_variable",
          "attributes": {
            "name": "Server Version",
            "description": "The version of Minecraft Vanilla to install. Use \"latest\" to install the latest version.",
            "env_variable": "VANILLA_VERSION",
            "default_value": "latest",
            "server_value": "latest",
            "is_editable": true,
            "rules": "required|string|between:3,15"
          }
        }
      ],
      "meta": {
        "startup_command": "java -Xms128M -Xmx512M -jar server.jar",
        "raw_startup_command": "java -Xms128M -Xmx\{\{ SERVER_MEMORY }}M -jar {\{ SERVER_JARFILE }}"
      }
    }

### **PUT** [ /variable ] Update Variable

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/startup/variable

Updates the specified variable

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "key": "SERVER_JARFILE",
      "value": "server.jar"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/startup/variable" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PUT \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "key": "SERVER_JARFILE",
      "value": "server.jar"
    }'

Example response - 200:

    {
      "object": "egg_variable",
      "attributes": {
        "name": "Server Jar File",
        "description": "The name of the server jarfile to run the server with.",
        "env_variable": "SERVER_JARFILE",
        "default_value": "server.jar",
        "server_value": "server.jar",
        "is_editable": true,
        "rules": "required|regex:\/^([\\w\\d._-]+)(\\.jar)$\/"
      }
    }

## [ /settings ] Settings

* * *

### **POST** [ /rename ] Rename server

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/settings/rename

Renames the server

# Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
name | required | string | New name for the server |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "Gaming"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/settings/rename" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "Gaming"
    }'

Example response - 204:

    // Successful

### **POST** [ /reinstall ] Reinstall server

    https://pterodactyl.file.properties/api/client/servers/1a7ce997/settings/reinstall

Renames the server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/client/servers/1a7ce997/settings/reinstall" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /api/application] Application

* * *

## [ /users ] Users

* * *

### **GET** [ / ] List users

    https://pterodactyl.file.properties/api/application/users

Retrieves all users

## Available Include parameters

Parameter | Description
---|---
servers | List of servers the user has access to

## Filters

Parameter
---
email
uuid
username
external_id

## Sort by

Parameter
---
id
uuid

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/users" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "user",
          "attributes": {
            "id": 1,
            "external_id": "RemoteId1",
            "uuid": "4de5a357-ed95-426b-aec1-8c328cfe9751",
            "username": "admin",
            "email": "example@example.com",
            "first_name": "Admin",
            "last_name": "User",
            "language": "en",
            "root_admin": true,
            "2fa": false,
            "created_at": "2019-12-22T04:43:29+00:00",
            "updated_at": "2020-07-13T13:10:23+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 2,
            "external_id": null,
            "uuid": "73f233ca-99e0-47a9-bd46-efd3296d7ad9",
            "username": "subuser1uxk",
            "email": "subuser1@example.com",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-06-12T22:18:43+00:00",
            "updated_at": "2020-06-12T22:18:43+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 3,
            "external_id": null,
            "uuid": "60a7aec3-e17d-4aa9-abb3-56d944d204b4",
            "username": "subuser2jvc",
            "email": "subuser2@example.com",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-06-12T22:31:41+00:00",
            "updated_at": "2020-06-12T22:31:41+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 4,
            "external_id": null,
            "uuid": "a14e9c5f-9c7a-448f-9106-58e2b5286de6",
            "username": "test",
            "email": "example2@example.com",
            "first_name": "Test",
            "last_name": "Admin",
            "language": "en",
            "root_admin": true,
            "2fa": false,
            "created_at": "2020-06-14T00:34:50+00:00",
            "updated_at": "2020-06-14T00:34:50+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 5,
            "external_id": null,
            "uuid": "1287632d-9224-40c0-906e-f543423400bc",
            "username": "subuser3bvo",
            "email": "subuser3@example.com",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-07-13T13:27:46+00:00",
            "updated_at": "2020-07-13T13:27:46+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 6,
            "external_id": null,
            "uuid": "2fcb6f7e-342a-423a-93a4-6111a237c0c7",
            "username": "geboc70057d6r",
            "email": "geboc70057@djemail.net",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-07-13T13:36:44+00:00",
            "updated_at": "2020-07-13T13:36:44+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 7,
            "external_id": null,
            "uuid": "b20e4e11-550f-4c52-893d-94fc8bc46a06",
            "username": "testidq",
            "email": "test@example.com",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-07-19T12:48:38+00:00",
            "updated_at": "2020-07-19T12:48:38+00:00"
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 7,
          "count": 7,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

Example response - 200:

    // GET /api/application/users?filter%5Bemail%5D=dane%40daneeveritt.com
    {
      "object": "list",
      "data": [
        {
          "object": "user",
          "attributes": {
            "id": 27,
            "external_id": null,
            "uuid": "18528bb9-8f60-45e2-adc6-f72611559fd7",
            "username": "hodor7wm",
            "email": "hodor@example.com",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-08-19T03:23:35+00:00",
            "updated_at": "2020-08-19T03:23:35+00:00"
          }
        },
        {
          "object": "user",
          "attributes": {
            "id": 26,
            "external_id": null,
            "uuid": "b83673f6-3387-4a37-97cd-dd3a4f508343",
            "username": "testfz0",
            "email": "test@example.com",
            "first_name": "Server",
            "last_name": "Subuser",
            "language": "en",
            "root_admin": false,
            "2fa": false,
            "created_at": "2020-08-19T03:15:51+00:00",
            "updated_at": "2020-08-19T03:15:51+00:00"
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 2,
          "count": 2,
          "per_page": 100,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **GET** [ /{user} ] User details

    https://pterodactyl.file.properties/api/application/users/1

Retrieves the specified user

## Available include parameters

Parameter | Description
---|---
servers | List of servers the user has access to

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/users/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "user",
      "attributes": {
        "id": 1,
        "external_id": "RemoteId1",
        "uuid": "4de5a357-ed95-426b-aec1-8c328cfe9751",
        "username": "admin",
        "email": "example@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "language": "en",
        "root_admin": true,
        "2fa": false,
        "created_at": "2019-12-22T04:43:29+00:00",
        "updated_at": "2020-07-13T13:10:23+00:00"
      }
    }

### **GET** [ /external/{external_id} ] User details

    https://pterodactyl.file.properties/api/application/users/external/RemoteId1

Retrieves the specified user by its external ID

## Available include parameters

Parameter | Description
---|---
servers | List of servers the user has access to

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/users/external/RemoteId1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "user",
      "attributes": {
        "id": 1,
        "external_id": "RemoteId1",
        "uuid": "4de5a357-ed95-426b-aec1-8c328cfe9751",
        "username": "admin",
        "email": "example@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "language": "en",
        "root_admin": true,
        "2fa": false,
        "created_at": "2019-12-22T04:43:29+00:00",
        "updated_at": "2020-07-13T13:10:23+00:00"
      }
    }

### **POST** [ / ] Create user

    https://pterodactyl.file.properties/api/application/users

Creates a new user

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "email": "example10@example.com",
      "username": "exampleuser",
      "first_name": "Example",
      "last_name": "User"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/users" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "email": "example10@example.com",
      "username": "exampleuser",
      "first_name": "Example",
      "last_name": "User"
    }'

Example response - 201:

    {
      "object": "user",
      "attributes": {
        "id": 9,
        "external_id": null,
        "uuid": "dac03ece-fd51-4e4b-bd4f-a79e3b2794f9",
        "username": "exampleuser",
        "email": "example10@example.com",
        "first_name": "Example",
        "last_name": "User",
        "language": "en",
        "root_admin": false,
        "2fa": false,
        "created_at": "2020-10-29T01:25:12+00:00",
        "updated_at": "2020-10-29T01:25:12+00:00"
      },
      "meta": {
        "resource": "https:\/\/pterodactyl.file.properties\/api\/application\/users\/9"
      }
    }

### **PATCH** [ / ] Update user

    https://pterodactyl.file.properties/api/application/users/9

Updates the user information

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "email": "example10@example.com",
      "username": "exampleuser",
      "first_name": "Example",
      "last_name": "User",
      "language": "en",
      "password": "New Password"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/users/9" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PATCH \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "email": "example10@example.com",
      "username": "exampleuser",
      "first_name": "Example",
      "last_name": "User",
      "language": "en",
      "password": "New Password"
    }'

Example response - 200:

    {
      "object": "user",
      "attributes": {
        "id": 9,
        "external_id": null,
        "uuid": "dac03ece-fd51-4e4b-bd4f-a79e3b2794f9",
        "username": "exampleuser",
        "email": "example10@example.com",
        "first_name": "Example",
        "last_name": "User",
        "language": "en",
        "root_admin": false,
        "2fa": false,
        "created_at": "2020-10-29T01:25:12+00:00",
        "updated_at": "2020-10-29T01:28:29+00:00"
      }
    }

### **DELETE** [ /{user} ] Delete user

    https://pterodactyl.file.properties/api/application/users/8

Deletes the specified user

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/users/8" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /nodes ] Nodes

* * *

### **GET** [ / ] List nodes

    https://pterodactyl.file.properties/api/application/nodes

Retrieves a list of nodes

## Available include parameters

Parameter | Description
---|---
allocations | List of allocations added to the node
location | Information about the location the node is assigned to
servers | List of servers on the node

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "node",
          "attributes": {
            "id": 1,
            "uuid": "1046d1d1-b8ef-4771-82b1-2b5946d33397",
            "public": true,
            "name": "Test",
            "description": "Test",
            "location_id": 1,
            "fqdn": "pterodactyl.file.properties",
            "scheme": "https",
            "behind_proxy": false,
            "maintenance_mode": false,
            "memory": 2048,
            "memory_overallocate": 0,
            "disk": 5000,
            "disk_overallocate": 0,
            "upload_size": 100,
            "daemon_listen": 8080,
            "daemon_sftp": 2022,
            "daemon_base": "\/srv\/daemon-data",
            "created_at": "2019-12-22T04:44:51+00:00",
            "updated_at": "2019-12-22T04:44:51+00:00"
          }
        },
        {
          "object": "node",
          "attributes": {
            "id": 3,
            "uuid": "71b15cf6-909a-4b60-aa04-abb4c8f98f61",
            "public": true,
            "name": "2",
            "description": "e",
            "location_id": 1,
            "fqdn": "pterodactyl.file.properties",
            "scheme": "https",
            "behind_proxy": false,
            "maintenance_mode": false,
            "memory": 100,
            "memory_overallocate": 0,
            "disk": 100,
            "disk_overallocate": 0,
            "upload_size": 100,
            "daemon_listen": 8080,
            "daemon_sftp": 2022,
            "daemon_base": "\/var\/lib\/pterodactyl\/volumes",
            "created_at": "2020-06-23T04:50:37+00:00",
            "updated_at": "2020-06-23T04:50:37+00:00"
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 2,
          "count": 2,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **GET** [ /{node} ] Node details

    https://pterodactyl.file.properties/api/application/nodes/1

Retrieves the specified node

## Available include parameters

Parameter | Description
---|---
allocations | List of allocations added to the node
location | Information about the location the node is assigned to
servers | List of servers on the node

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "node",
      "attributes": {
        "id": 1,
        "uuid": "1046d1d1-b8ef-4771-82b1-2b5946d33397",
        "public": true,
        "name": "Test",
        "description": "Test",
        "location_id": 1,
        "fqdn": "pterodactyl.file.properties",
        "scheme": "https",
        "behind_proxy": false,
        "maintenance_mode": false,
        "memory": 2048,
        "memory_overallocate": 0,
        "disk": 5000,
        "disk_overallocate": 0,
        "upload_size": 100,
        "daemon_listen": 8080,
        "daemon_sftp": 2022,
        "daemon_base": "\/srv\/daemon-data",
        "created_at": "2019-12-22T04:44:51+00:00",
        "updated_at": "2019-12-22T04:44:51+00:00"
      }
    }

### **GET** [ /{node}/configuration ] Node configuration

    https://pterodactyl.file.properties/api/application/nodes/1/configuration

Displays the Wings configuration

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1/configuration" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "debug": false,
      "uuid": "1046d1d1-b8ef-4771-82b1-2b5946d33397",
      "token_id": "iAcosCn1KCAgVjVO",
      "token": "FanPzLCptUxkGow3vi7Z",
      "api": {
        "host": "0.0.0.0",
        "port": 8080,
        "ssl": {
          "enabled": true,
          "cert": "\/etc\/letsencrypt\/live\/pterodactyl.file.properties\/fullchain.pem",
          "key": "\/etc\/letsencrypt\/live\/pterodactyl.file.properties\/privkey.pem"
        },
        "upload_limit": 100
      },
      "system": {
        "data": "\/srv\/daemon-data",
        "sftp": {
          "bind_port": 2022
        }
      },
      "remote": "https:\/\/pterodactyl.file.properties"
    }

### **POST** [ / ] Create node

    https://pterodactyl.file.properties/api/application/nodes

Creates a new node

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "New Node",
      "location_id": 1,
      "fqdn": "node2.example.com",
      "scheme": "https",
      "memory": 10240,
      "memory_overallocate": 0,
      "disk": 50000,
      "disk_overallocate": 0,
      "upload_size": 100,
      "daemon_sftp": 2022,
      "daemon_listen": 8080
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "New Node",
      "location_id": 1,
      "fqdn": "node2.example.com",
      "scheme": "https",
      "memory": 10240,
      "memory_overallocate": 0,
      "disk": 50000,
      "disk_overallocate": 0,
      "upload_size": 100,
      "daemon_sftp": 2022,
      "daemon_listen": 8080
    }'

Example response - 201:

    {
      "object": "node",
      "attributes": {
        "id": 4,
        "uuid": "4158cfe9-2aa8-4812-bf6e-d88beeb08e98",
        "public": true,
        "name": "New Node",
        "description": null,
        "location_id": 1,
        "fqdn": "node2.example.com",
        "scheme": "https",
        "behind_proxy": false,
        "maintenance_mode": false,
        "memory": 10240,
        "memory_overallocate": 0,
        "disk": 50000,
        "disk_overallocate": 0,
        "upload_size": 100,
        "daemon_listen": 8080,
        "daemon_sftp": 2022,
        "daemon_base": "\/var\/lib\/pterodactyl\/volumes",
        "created_at": "2020-10-29T01:17:38+00:00",
        "updated_at": "2020-10-29T01:17:38+00:00",
        "allocated_resources": {
          "memory": 0,
          "disk": 0
        }
      },
      "meta": {
        "resource": "https:\/\/pterodactyl.file.properties\/api\/application\/nodes\/4"
      }
    }

### **PATCH** [ /{node} ] Update node

    https://pterodactyl.file.properties/api/application/nodes/1

Updates the node details

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "Test Renamed",
      "description": "Test",
      "location_id": 1,
      "fqdn": "pterodactyl.file.properties",
      "scheme": "https",
      "behind_proxy": false,
      "maintenance_mode": false,
      "memory": 2048,
      "memory_overallocate": 0,
      "disk": 5000,
      "disk_overallocate": 0,
      "upload_size": 100,
      "daemon_sftp": 2022,
      "daemon_listen": 8080
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PATCH \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "Test Renamed",
      "description": "Test",
      "location_id": 1,
      "fqdn": "pterodactyl.file.properties",
      "scheme": "https",
      "behind_proxy": false,
      "maintenance_mode": false,
      "memory": 2048,
      "memory_overallocate": 0,
      "disk": 5000,
      "disk_overallocate": 0,
      "upload_size": 100,
      "daemon_sftp": 2022,
      "daemon_listen": 8080
    }'

Example response - 200:

    {
      "object": "node",
      "attributes": {
        "id": 1,
        "uuid": "1046d1d1-b8ef-4771-82b1-2b5946d33397",
        "public": true,
        "name": "Test Renamed",
        "description": "Test",
        "location_id": 1,
        "fqdn": "pterodactyl.file.properties",
        "scheme": "https",
        "behind_proxy": false,
        "maintenance_mode": false,
        "memory": 2048,
        "memory_overallocate": 0,
        "disk": 5000,
        "disk_overallocate": 0,
        "upload_size": 100,
        "daemon_listen": 8080,
        "daemon_sftp": 2022,
        "daemon_base": "\/var\/lib\/pterodactyl\/volumes",
        "created_at": "2019-12-22T04:44:51+00:00",
        "updated_at": "2020-10-29T01:20:23+00:00",
        "mounts": [],
        "allocated_resources": {
          "memory": 640,
          "disk": 700
        }
      }
    }

### **DELETE** [ /{node} ] Delete node

    https://pterodactyl.file.properties/api/application/nodes/1

Deletes the specified node

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /{node}/allocations ] Allocations

* * *

### **GET** [ / ] List allocations

    https://pterodactyl.file.properties/api/application/nodes/1/allocations

Lists allocations added to the node

## Available include parameters

Parameter | Description
---|---
node | Information about the node the allocation belongs to
server | Information about the server the allocation belongs to

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1/allocations" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "allocation",
          "attributes": {
            "id": 1,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25565,
            "notes": null,
            "assigned": true
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 2,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25566,
            "notes": "Votifier",
            "assigned": true
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 3,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25567,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 4,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25568,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 5,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25569,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 6,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25570,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 8,
            "ip": "10.0.0.1",
            "alias": null,
            "port": 25565,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 9,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25571,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 10,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25572,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 11,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25573,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 12,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25574,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 13,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25575,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 14,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25576,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 15,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25577,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 16,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25578,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 17,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25579,
            "notes": null,
            "assigned": false
          }
        },
        {
          "object": "allocation",
          "attributes": {
            "id": 18,
            "ip": "45.86.168.218",
            "alias": null,
            "port": 25580,
            "notes": null,
            "assigned": false
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 17,
          "count": 17,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **POST** [ / ] Create allocations

    https://pterodactyl.file.properties/api/application/nodes/1/allocations

Adds an allocation to the node

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
ip | required | string | IP address for the allocations |
ports | required | object | Object containing the ports to add |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "ip": "10.0.0.1",
      "ports": [
        "25565"
      ]
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1/allocations" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "ip": "10.0.0.1",
      "ports": [
        "25565"
      ]
    }'

Example response - 204:

    // Successful

### **DELETE** [ /{allocation} ] Delete allocation

    https://pterodactyl.file.properties/api/application/nodes/1/allocations/18

Deletes the specified allocation

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nodes/1/allocations/18" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /locations ] Locations

* * *

### **GET** [ / ] List locations

    https://pterodactyl.file.properties/api/application/locations

Retrieves all locations

# Available include parameters

Parameter | Description
---|---
nodes | List of nodes assigned to the location
servers | List of servers in the location

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/locations" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "location",
          "attributes": {
            "id": 1,
            "short": "GB",
            "long": "London Datacenter",
            "updated_at": "2020-06-13T21:16:58+00:00",
            "created_at": "2019-12-22T04:44:18+00:00"
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 1,
          "count": 1,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **GET** [ /{location} ] Location details

    https://pterodactyl.file.properties/api/application/locations/1

Retrieves the specified location

# Available include parameters

Parameter | Description
---|---
nodes | List of nodes assigned to the location
servers | List of servers in the location

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/locations/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "location",
      "attributes": {
        "id": 1,
        "short": "Test",
        "long": "Test",
        "updated_at": "2019-12-22T04:44:18+00:00",
        "created_at": "2019-12-22T04:44:18+00:00"
      }
    }

### **POST** [ / ] Create location

    https://pterodactyl.file.properties/api/application/locations

Creates a new location

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
short | required | string | Location identifier |
long | optional | string | Location description |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "short": "GB",
      "long": "London Datacenter"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/locations" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "short": "GB",
      "long": "London Datacenter"
    }'

Example response - 200:

    {
      "object": "location",
      "attributes": {
        "id": 3,
        "short": "G",
        "long": "London Datacenter",
        "updated_at": "2020-06-13T20:44:48+00:00",
        "created_at": "2020-06-13T20:44:48+00:00"
      },
      "meta": {
        "resource": "https:\/\/pterodactyl.file.properties\/api\/application\/locations\/3"
      }
    }

### **PATCH** [ / ] Update location

    https://pterodactyl.file.properties/api/application/locations/1

Updates the specified location

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "short": "GB",
      "long": "London Datacenter"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/locations/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PATCH \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "short": "GB",
      "long": "London Datacenter"
    }'

Example response - 200:

    {
      "object": "location",
      "attributes": {
        "id": 1,
        "short": "GB",
        "long": "London Datacenter",
        "updated_at": "2020-06-13T21:16:58+00:00",
        "created_at": "2019-12-22T04:44:18+00:00"
      }
    }

### **DELETE** [ /{location} ] Delete location

    https://pterodactyl.file.properties/api/application/locations/3

Deletes the specified location

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/locations/3" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /servers ] Servers

* * *

### **GET** [ / ] List servers

    https://pterodactyl.file.properties/api/application/servers

Retrieves all servers

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "server",
          "attributes": {
            "id": 5,
            "external_id": "RemoteId1",
            "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "identifier": "1a7ce997",
            "name": "Wuhu Island",
            "description": "Matt from Wii Sports",
            "suspended": false,
            "limits": {
              "memory": 512,
              "swap": 0,
              "disk": 200,
              "io": 500,
              "cpu": 0,
              "threads": null
            },
            "feature_limits": {
              "databases": 5,
              "allocations": 5,
              "backups": 2
            },
            "user": 1,
            "node": 1,
            "allocation": 1,
            "nest": 1,
            "egg": 5,
            "pack": null,
            "container": {
              "startup_command": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
              "image": "quay.io\/pterodactyl\/core:java",
              "installed": true,
              "environment": {
                "SERVER_JARFILE": "server.jar",
                "VANILLA_VERSION": "latest",
                "STARTUP": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
                "P_SERVER_LOCATION": "Test",
                "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca"
              }
            },
            "updated_at": "2020-06-13T04:20:53+00:00",
            "created_at": "2019-12-23T06:46:27+00:00",
            "relationships": {
              "databases": {
                "object": "list",
                "data": [
                  {
                    "object": "databases",
                    "attributes": {
                      "id": 1,
                      "server": 5,
                      "host": 4,
                      "database": "s5_perms",
                      "username": "u5_QsIAp1jhvS",
                      "remote": "%",
                      "max_connections": 0,
                      "created_at": "2020-06-12T23:00:13+01:00",
                      "updated_at": "2020-06-12T23:00:13+01:00"
                    }
                  },
                  {
                    "object": "databases",
                    "attributes": {
                      "id": 2,
                      "server": 5,
                      "host": 4,
                      "database": "s5_coreprotect",
                      "username": "u5_2jtJx1nO1d",
                      "remote": "%",
                      "max_connections": 0,
                      "created_at": "2020-06-12T23:00:20+01:00",
                      "updated_at": "2020-06-12T23:00:20+01:00"
                    }
                  }
                ]
              }
            }
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 1,
          "count": 1,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **GET** [ /{server} ] Server details

    https://pterodactyl.file.properties/api/application/servers/5

Retrieves the specified server

## Available include parameters

Parameter | Description
---|---
allocations | List of allocations assigned to the server
user | Information about the server owner
subusers | List of users added to the server
pack | Information about the server pack
nest | Information about the server's egg nest
egg | Information about the server's egg
variables | List of server variables
location | Information about server's node location
node | Information about the server's node
databases | List of databases on the server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "server",
      "attributes": {
        "id": 5,
        "external_id": "RemoteId1",
        "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
        "identifier": "1a7ce997",
        "name": "Gaming",
        "description": "Matt from Wii Sports",
        "suspended": false,
        "limits": {
          "memory": 512,
          "swap": 0,
          "disk": 200,
          "io": 500,
          "cpu": 0,
          "threads": null
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 5,
          "backups": 2
        },
        "user": 1,
        "node": 1,
        "allocation": 1,
        "nest": 1,
        "egg": 5,
        "pack": null,
        "container": {
          "startup_command": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
          "image": "quay.io\/pterodactyl\/core:java",
          "installed": true,
          "environment": {
            "SERVER_JARFILE": "server.jar",
            "VANILLA_VERSION": "latest",
            "STARTUP": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
            "P_SERVER_LOCATION": "GB",
            "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "P_SERVER_ALLOCATION_LIMIT": 5
          }
        },
        "updated_at": "2020-07-19T15:22:39+00:00",
        "created_at": "2019-12-23T06:46:27+00:00"
      }
    }

### **GET** [ /external/{external_id} ] Server details

    https://pterodactyl.file.properties/api/application/servers/external/RemoteId1

Retrieves a server by its external ID

## Available include parameters

Parameter | Description
---|---
allocations | List of allocations assigned to the server
user | Information about the server owner
subusers | List of users added to the server
pack | Information about the server pack
nest | Information about the server's egg nest
egg | Information about the server's egg
variables | List of server variables
location | Information about server's node location
node | Information about the server's node
databases | List of databases on the server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/external/RemoteId1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response:

    {
      "object": "server",
      "attributes": {
        "id": 5,
        "external_id": "RemoteId1",
        "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
        "identifier": "1a7ce997",
        "name": "Gaming",
        "description": "Matt from Wii Sports",
        "suspended": false,
        "limits": {
          "memory": 512,
          "swap": 0,
          "disk": 200,
          "io": 500,
          "cpu": 0,
          "threads": null
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 5,
          "backups": 2
        },
        "user": 1,
        "node": 1,
        "allocation": 1,
        "nest": 1,
        "egg": 5,
        "pack": null,
        "container": {
          "startup_command": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
          "image": "quay.io\/pterodactyl\/core:java",
          "installed": true,
          "environment": {
            "SERVER_JARFILE": "server.jar",
            "VANILLA_VERSION": "latest",
            "STARTUP": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
            "P_SERVER_LOCATION": "GB",
            "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "P_SERVER_ALLOCATION_LIMIT": 5
          }
        },
        "updated_at": "2020-07-19T15:22:39+00:00",
        "created_at": "2019-12-23T06:46:27+00:00"
      }
    }

### **PATCH** [ /{server}/details ] Update details

    https://pterodactyl.file.properties/api/application/servers/5/details

Updates the server details

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
name | required | string | Name for the server |
user | required | number | ID of the user which the server belongs to |
external_id |  | string | External ID of the server |
description |  | string | Description of the server |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "Gaming",
      "user": 1,
      "external_id": "RemoteID1",
      "description": "Matt from Wii Sports"
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/details" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PATCH \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "Gaming",
      "user": 1,
      "external_id": "RemoteID1",
      "description": "Matt from Wii Sports"
    }'

Example response:

    {
      "object": "server",
      "attributes": {
        "id": 5,
        "external_id": "RemoteID1",
        "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
        "identifier": "1a7ce997",
        "name": "Gaming",
        "description": "Matt from Wii Sports",
        "suspended": false,
        "limits": {
          "memory": 512,
          "swap": 0,
          "disk": 200,
          "io": 500,
          "cpu": 0,
          "threads": null
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 5,
          "backups": 2
        },
        "user": 1,
        "node": 1,
        "allocation": 1,
        "nest": 1,
        "egg": 5,
        "container": {
          "startup_command": "java -Xms128M -Xmx2014M -jar server.jar",
          "image": "quay.io\/pterodactyl\/core:java",
          "installed": true,
          "environment": {
            "SERVER_JARFILE": "server.jar",
            "VANILLA_VERSION": "latest",
            "STARTUP": "java -Xms128M -Xmx2048M -jar server.jar",
            "P_SERVER_LOCATION": "GB",
            "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "P_SERVER_ALLOCATION_LIMIT": 5
          }
        },
        "updated_at": "2020-11-04T21:11:26+00:00",
        "created_at": "2019-12-23T06:46:27+00:00"
      }
    }

### **PATCH** [ /{server}/build ] Update build

    https://pterodactyl.file.properties/api/application/servers/5/build

Updates the server build information

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
allocation | required | number | ID of primary allocation |
memory | required_without | number | The maximum amount of memory allowed for this container. Setting this to 0 will allow unlimited memory in a container. |
swap | required_without | number | Setting this to 0 will disable swap space on this server. Setting to -1 will allow unlimited swap. |
io | required_without | number | IO performance of this server relative to other running containers |
cpu | required_without | number | Each physical core on the system is considered to be 100%. Setting this value to 0 will allow a server to use CPU time without restrictions. |
disk | required_without | number | This server will not be allowed to boot if it is using more than this amount of space. If a server goes over this limit while running it will be safely stopped and locked until enough space is available. Set to 0 to allow unlimited disk usage. |
threads |  | number | Enter the specific CPU cores that this process can run on, or leave blank to allow all cores. This can be a single number, or a comma seperated list. Example: 0, 0-1,3, or 0,1,3,4. |
feature_limits | required | object |  |
feature_limits.databases | present | number | The total number of databases a user is allowed to create for this server. |
feature_limits.backups | present | number | The total number of allocations a user is allowed to create for this server. |
feature_limits.allocations |  | number | The total number of allocations a user is allowed to create for this server. |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "allocation": 1,
      "memory": 512,
      "swap": 0,
      "disk": 200,
      "io": 500,
      "cpu": 0,
      "threads": null,
      "feature_limits": {
        "databases": 5,
        "allocations": 5,
        "backups": 2
      }
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/build" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PATCH \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "allocation": 1,
      "memory": 512,
      "swap": 0,
      "disk": 200,
      "io": 500,
      "cpu": 0,
      "threads": null,
      "feature_limits": {
        "databases": 5,
        "allocations": 5,
        "backups": 2
      }
    }'

Example response:

    {
      "object": "server",
      "attributes": {
        "id": 5,
        "external_id": "RemoteID1",
        "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
        "identifier": "1a7ce997",
        "name": "Gaming",
        "description": "Matt from Wii Sports",
        "suspended": false,
        "limits": {
          "memory": 512,
          "swap": 0,
          "disk": 200,
          "io": 500,
          "cpu": 0,
          "threads": null
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 5,
          "backups": 2
        },
        "user": 1,
        "node": 1,
        "allocation": 1,
        "nest": 1,
        "egg": 5,
        "container": {
          "startup_command": "java -Xms128M -Xmx2014M -jar server.jar",
          "image": "quay.io\/pterodactyl\/core:java",
          "installed": true,
          "environment": {
            "SERVER_JARFILE": "server.jar",
            "VANILLA_VERSION": "latest",
            "STARTUP": "java -Xms128M -Xmx2048M -jar server.jar",
            "P_SERVER_LOCATION": "GB",
            "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "P_SERVER_ALLOCATION_LIMIT": 5
          }
        },
        "updated_at": "2020-11-04T21:11:26+00:00",
        "created_at": "2019-12-23T06:46:27+00:00"
      }
    }

### **PATCH** [ /{server}/startup ] Update startup

    https://pterodactyl.file.properties/api/application/servers/5/startup

Updates the server startup information

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
startup | required | string | Edit your server's startup command here. |
environment | present | object | Environment variables that the egg requires/supports |
egg | required | string | ID of the egg to use |
image | required | required | The Docker image to use for this server |
skip_scripts | present | required | If enabled, if the Egg has an install script, it will NOT be ran during install. |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
      "environment": {
        "SERVER_JARFILE": "server.jar",
        "VANILLA_VERSION": "latest"
      },
      "egg": 5,
      "image": "quay.io/pterodactyl/core:java",
      "skip_scripts": false
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/startup" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X PATCH \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
      "environment": {
        "SERVER_JARFILE": "server.jar",
        "VANILLA_VERSION": "latest"
      },
      "egg": 5,
      "image": "quay.io/pterodactyl/core:java",
      "skip_scripts": false
    }'

Example response:

    {
      "object": "server",
      "attributes": {
        "id": 5,
        "external_id": "RemoteID1",
        "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
        "identifier": "1a7ce997",
        "name": "Gaming",
        "description": "Matt from Wii Sports",
        "suspended": false,
        "limits": {
          "memory": 512,
          "swap": 0,
          "disk": 200,
          "io": 500,
          "cpu": 0,
          "threads": null
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 5,
          "backups": 2
        },
        "user": 1,
        "node": 1,
        "allocation": 1,
        "nest": 1,
        "egg": 5,
        "container": {
          "startup_command": "java -Xms128M -Xmx2014M -jar server.jar",
          "image": "quay.io\/pterodactyl\/core:java",
          "installed": true,
          "environment": {
            "SERVER_JARFILE": "server.jar",
            "VANILLA_VERSION": "latest",
            "STARTUP": "java -Xms128M -Xmx2048M -jar server.jar",
            "P_SERVER_LOCATION": "GB",
            "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca",
            "P_SERVER_ALLOCATION_LIMIT": 5
          }
        },
        "updated_at": "2020-11-04T21:11:26+00:00",
        "created_at": "2019-12-23T06:46:27+00:00"
      }
    }

### **POST** [ / ] Create server

    https://pterodactyl.file.properties/api/application/servers

Creates a new server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "name": "Building",
      "user": 1,
      "egg": 1,
      "docker_image": "quay.io/pterodactyl/core:java",
      "startup": "java -Xms128M -Xmx128M -jar server.jar",
      "environment": {
        "BUNGEE_VERSION": "latest",
        "SERVER_JARFILE": "server.jar"
      },
      "limits": {
        "memory": 128,
        "swap": 0,
        "disk": 512,
        "io": 500,
        "cpu": 100
      },
      "feature_limits": {
        "databases": 5,
        "backups": 1
      },
      "allocation": {
        "default": 17
      }
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "name": "Building",
      "user": 1,
      "egg": 1,
      "docker_image": "quay.io/pterodactyl/core:java",
      "startup": "java -Xms128M -Xmx128M -jar server.jar",
      "environment": {
        "BUNGEE_VERSION": "latest",
        "SERVER_JARFILE": "server.jar"
      },
      "limits": {
        "memory": 128,
        "swap": 0,
        "disk": 512,
        "io": 500,
        "cpu": 100
      },
      "feature_limits": {
        "databases": 5,
        "backups": 1
      },
      "allocation": {
        "default": 17
      }
    }'

Example response - 201:

    {
      "object": "server",
      "attributes": {
        "id": 7,
        "external_id": null,
        "uuid": "d557c19c-8b21-4456-a9e5-181beda429f4",
        "identifier": "d557c19c",
        "name": "Building",
        "description": "",
        "suspended": false,
        "limits": {
          "memory": 128,
          "swap": 0,
          "disk": 512,
          "io": 500,
          "cpu": 100,
          "threads": null
        },
        "feature_limits": {
          "databases": 5,
          "allocations": 0,
          "backups": 1
        },
        "user": 1,
        "node": 1,
        "allocation": 17,
        "nest": 1,
        "egg": 1,
        "container": {
          "startup_command": "java -Xms128M -Xmx128M -jar server.jar",
          "image": "quay.io\/pterodactyl\/core:java",
          "installed": false,
          "environment": {
            "BUNGEE_VERSION": "latest",
            "SERVER_JARFILE": "server.jar",
            "STARTUP": "java -Xms128M -Xmx128M -jar server.jar",
            "P_SERVER_LOCATION": "GB",
            "P_SERVER_UUID": "d557c19c-8b21-4456-a9e5-181beda429f4",
            "P_SERVER_ALLOCATION_LIMIT": 0
          }
        },
        "updated_at": "2020-10-29T01:38:59+00:00",
        "created_at": "2020-10-29T01:38:59+00:00"
      }
    }

### **POST** [ /{server}/suspend ] Suspend server

    https://pterodactyl.file.properties/api/application/servers/5/suspend

Suspends the specified server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/suspend" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

### **POST** [ /{server}/unsuspend ] Unsuspend server

    https://pterodactyl.file.properties/api/application/servers/5/unsuspend

Unuspends the specified

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/unsuspend" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

### **POST** [ /{server}/reinstall ] Reinstall server

    https://pterodactyl.file.properties/api/application/servers/5/reinstall

Reinstalls the specified server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/reinstall" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

### **DELETE** [ /{server} ] Delete server

    https://pterodactyl.file.properties/api/application/servers/1

Deletes the specified server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

### **DELETE** [ /{server}/{force?} ] Force delete server

    https://pterodactyl.file.properties/api/application/servers/1/force

Forcefully deletes the specified server

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/1/force" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /{server}/databases ] Database Management

* * *

### **GET** [ / ] List databases

    https://pterodactyl.file.properties/api/application/servers/5/databases?include=password,host

Retrieves all databases on a server

## Available include parameters

Parameter | Description
---|---
password | Includes the database user password
host | Information about the database host

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/databases?include=password,host" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "server_database",
          "attributes": {
            "id": 1,
            "server": 5,
            "host": 4,
            "database": "s5_perms",
            "username": "u5_QsIAp1jhvS",
            "remote": "%",
            "max_connections": 0,
            "created_at": "2020-06-12T23:00:13+01:00",
            "updated_at": "2020-06-12T23:00:13+01:00",
            "relationships": {
              "password": {
                "object": "database_password",
                "attributes": {
                  "password": ".FjJ!5w945L3tuG4DrSxF+T@"
                }
              },
              "host": {
                "object": "database_host",
                "attributes": {
                  "id": 4,
                  "name": "MariaDB",
                  "host": "127.0.0.1",
                  "port": 3306,
                  "username": "pterodactyluser",
                  "node": 1,
                  "created_at": "2020-06-12T22:59:25+01:00",
                  "updated_at": "2020-06-12T22:59:25+01:00"
                }
              }
            }
          }
        },
        {
          "object": "server_database",
          "attributes": {
            "id": 2,
            "server": 5,
            "host": 4,
            "database": "s5_coreprotect",
            "username": "u5_2jtJx1nO1d",
            "remote": "%",
            "max_connections": 0,
            "created_at": "2020-06-12T23:00:20+01:00",
            "updated_at": "2020-06-12T23:00:20+01:00",
            "relationships": {
              "password": {
                "object": "database_password",
                "attributes": {
                  "password": "4=rv^0vHuOPSHCfj!tM1OlMC"
                }
              },
              "host": {
                "object": "database_host",
                "attributes": {
                  "id": 4,
                  "name": "MariaDB",
                  "host": "127.0.0.1",
                  "port": 3306,
                  "username": "pterodactyluser",
                  "node": 1,
                  "created_at": "2020-06-12T22:59:25+01:00",
                  "updated_at": "2020-06-12T22:59:25+01:00"
                }
              }
            }
          }
        }
      ]
    }

### **GET** [ /{database} ] Database details

    https://pterodactyl.file.properties/api/application/servers/5/databases/1

Retrieves the specified database

## Available include parameters

Parameter | Description
---|---
password | Includes the database user password
host | Information about the database host

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/databases/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "server_database",
      "attributes": {
        "id": 1,
        "server": 5,
        "host": 4,
        "database": "s5_perms",
        "username": "u5_QsIAp1jhvS",
        "remote": "%",
        "max_connections": 0,
        "created_at": "2020-06-12T23:00:13+01:00",
        "updated_at": "2020-06-12T23:00:13+01:00"
      }
    }

### **POST** [ / ] Create database

    https://pterodactyl.file.properties/api/application/servers/5/databases

Creates a new database on the specified server

## Fields

Name | Required? | Type | Description | Rules
---|---|---|---|---
database | required | string | Name for database |
remote | database | string | Permitted remotes that can access the database |
host | database | number | ID of the database host to use |

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

Body json

    {
      "database": "matches",
      "remote": "%",
      "host": 4
    }

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/databases" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D' \
      -d '{
      "database": "matches",
      "remote": "%",
      "host": 4
    }'

Example response - 200:

    {
      "object": "server_database",
      "attributes": {
        "id": 6,
        "server": 5,
        "host": 4,
        "database": "s5_matches",
        "username": "u5_LhG3aGWBtk",
        "remote": "%",
        "max_connections": null,
        "created_at": "2020-11-04T21:00:42+00:00",
        "updated_at": "2020-11-04T21:00:42+00:00"
      },
      "meta": {
        "resource": "https:\/\/pterodactyl.file.properties\/api\/application\/servers\/5\/databases\/6"
      }
    }

### **POST** [ /{database}/reset-password ] Reset password

    https://pterodactyl.file.properties/api/application/servers/5/databases/1/reset-password

Rotates the password of the database

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/databases/1/reset-password" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X POST \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

### **DELETE** [ /{database} ] Delete database

    https://pterodactyl.file.properties/api/application/servers/5/databases/1

Deletes the specified database

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/servers/5/databases/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X DELETE \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 204:

    // Successful

## [ /nests ] Nests

* * *

### **GET** [ / ] List nests

    https://pterodactyl.file.properties/api/application/nests

Retrieves all nests

# Available include parameters

Parameter | Description
---|---
eggs | List of eggs in the location
servers | List of servers in the location

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nests" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "nest",
          "attributes": {
            "id": 1,
            "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
            "author": "support@pterodactyl.io",
            "name": "Minecraft",
            "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00"
          }
        },
        {
          "object": "nest",
          "attributes": {
            "id": 2,
            "uuid": "5246d226-e8e8-46f5-b624-e99cf1a68c9a",
            "author": "support@pterodactyl.io",
            "name": "Source Engine",
            "description": "Includes support for most Source Dedicated Server games.",
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00"
          }
        },
        {
          "object": "nest",
          "attributes": {
            "id": 3,
            "uuid": "0eb05bf7-3a00-4b1d-bef5-a6d8d7375e44",
            "author": "support@pterodactyl.io",
            "name": "Voice Servers",
            "description": "Voice servers such as Mumble and Teamspeak 3.",
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00"
          }
        },
        {
          "object": "nest",
          "attributes": {
            "id": 4,
            "uuid": "e2a21c82-7175-4db0-9510-8d1ed525b2bf",
            "author": "support@pterodactyl.io",
            "name": "Rust",
            "description": "Rust - A game where you must fight to survive.",
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00"
          }
        }
      ],
      "meta": {
        "pagination": {
          "total": 4,
          "count": 4,
          "per_page": 50,
          "current_page": 1,
          "total_pages": 1,
          "links": {}
        }
      }
    }

### **GET** [ /{nest} ] Nest details

    https://pterodactyl.file.properties/api/application/nests/1

Retrieves the specified nests

# Available include parameters

Parameter | Description
---|---
eggs | List of eggs in the location
servers | List of servers in the location

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nests/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "nest",
      "attributes": {
        "id": 1,
        "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
        "author": "support@pterodactyl.io",
        "name": "Minecraft",
        "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
        "created_at": "2019-12-22T04:42:51+00:00",
        "updated_at": "2019-12-22T04:42:51+00:00"
      }
    }

## [ /{nest}/eggs ] Eggs Management

* * *

### **GET** [ / ] List eggs

    https://pterodactyl.file.properties/api/application/nests/1/eggs?include=nest,servers

Retrieves a list of eggs

## Available include parameters

Parameter | Description
---|---
nest | Information about the nest that owns the egg
servers | List of servers using the egg
config | Config options of the egg
script | Egg install script
variables | List of egg variables

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nests/1/eggs?include=nest,servers" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "list",
      "data": [
        {
          "object": "egg",
          "attributes": {
            "id": 1,
            "uuid": "695648dd-01a3-4ced-b075-d4ec4fb9fbf4",
            "name": "Bungeecord",
            "nest": 1,
            "author": "support@pterodactyl.io",
            "description": "For a long time, Minecraft server owners have had a dream that encompasses a free, easy, and reliable way to connect multiple Minecraft servers together. BungeeCord is the answer to said dream. Whether you are a small server wishing to string multiple game-modes together, or the owner of the ShotBow Network, BungeeCord is the ideal solution for you. With the help of BungeeCord, you will be able to unlock your community's full potential.",
            "docker_image": "quay.io\/pterodactyl\/core:java",
            "config": {
              "files": {
                "config.yml": {
                  "parser": "yaml",
                  "find": {
                    "listeners[0].query_enabled": true,
                    "listeners[0].query_port": "{{server.build.default.port}}",
                    "listeners[0].host": "0.0.0.0:{{server.build.default.port}}",
                    "servers.*.address": {
                      "127.0.0.1": "{{config.docker.interface}}",
                      "localhost": "{{config.docker.interface}}"
                    }
                  }
                }
              },
              "startup": {
                "done": "Listening on ",
                "userInteraction": [
                  "Listening on \/0.0.0.0:25577"
                ]
              },
              "stop": "end",
              "logs": {
                "custom": false,
                "location": "proxy.log.0"
              },
              "extends": null
            },
            "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
            "script": {
              "privileged": true,
              "install": "#!\/bin\/ash\n# Bungeecord Installation Script\n#\n# Server Files: \/mnt\/server\napk update\napk add curl\n\ncd \/mnt\/server\n\nif [ -z \"${BUNGEE_VERSION}\" ] || [ \"${BUNGEE_VERSION}\" == \"latest\" ]; then\n    BUNGEE_VERSION=\"lastStableBuild\"\nfi\n\ncurl -o ${SERVER_JARFILE} https:\/\/ci.md-5.net\/job\/BungeeCord\/${BUNGEE_VERSION}\/artifact\/bootstrap\/target\/BungeeCord.jar",
              "entry": "ash",
              "container": "alpine:3.9",
              "extends": null
            },
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00",
            "relationships": {
              "nest": {
                "object": "nest",
                "attributes": {
                  "id": 1,
                  "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
                  "author": "support@pterodactyl.io",
                  "name": "Minecraft",
                  "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
                  "created_at": "2019-12-22T04:42:51+00:00",
                  "updated_at": "2019-12-22T04:42:51+00:00"
                }
              },
              "servers": {
                "object": "list",
                "data": []
              }
            }
          }
        },
        {
          "object": "egg",
          "attributes": {
            "id": 2,
            "uuid": "7f8736d8-fd99-465f-8c3e-cb4d42c18541",
            "name": "Forge Minecraft",
            "nest": 1,
            "author": "support@pterodactyl.io",
            "description": "Minecraft Forge Server. Minecraft Forge is a modding API (Application Programming Interface), which makes it easier to create mods, and also make sure mods are compatible with each other.",
            "docker_image": "quay.io\/pterodactyl\/core:java",
            "config": {
              "files": {
                "server.properties": {
                  "parser": "properties",
                  "find": {
                    "server-ip": "0.0.0.0",
                    "enable-query": "true",
                    "server-port": "{{server.build.default.port}}",
                    "query.port": "{{server.build.default.port}}"
                  }
                }
              },
              "startup": {
                "done": ")! For help, type ",
                "userInteraction": [
                  "Go to eula.txt for more info."
                ]
              },
              "stop": "stop",
              "logs": {
                "custom": false,
                "location": "logs\/latest.log"
              },
              "extends": null
            },
            "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
            "script": {
              "privileged": true,
              "install": "#!\/bin\/bash\r\n# Forge Installation Script\r\n#\r\n# Server Files: \/mnt\/server\r\napt update\r\napt install -y curl\r\n\r\n#Fetching version\r\nif [ -z \"$MC_VERSION\" ] || [ \"$MC_VERSION\" == \"latest\" ]; then\r\n  echo \"Fetching latest\"\r\n  MC_VERSION=$(curl -sl https:\/\/files.minecraftforge.net\/maven\/net\/minecraftforge\/forge\/index.html | grep -A 2 \"Latest\" | awk NF=NF RS= OFS=\" \" | grep -o -e '[1].[0-9]*.[0-9]* - [0-9]*.[0-9]*.[0-9]*.[0-9]*' | sed 's\/ \/\/g')\r\nelif [[ ! \"$MC_VERSION\" =~ - ]]; then\r\n  echo \"Fetching latest from version $MC_VERSION\"\r\n  MC_VERSION=$(curl -sl https:\/\/files.minecraftforge.net\/maven\/net\/minecraftforge\/forge\/index_$MC_VERSION.html | grep -A 2 \"Latest\" | awk NF=NF RS= OFS=\" \" | grep -o -e '[1].[0-9]*.[0-9]* - [0-9]*.[0-9]*.[0-9]*.[0-9]*' | sed 's\/ \/\/g')\r\nfi\r\n\r\n#Checking if forge version valid\r\nif [[ ! \"$MC_VERSION\" =~ [1].[0-9]*.[0-9]*-[0-9]*.[0-9]*.[0-9]*.[0-9]* ]]; then\r\n    echo \"!!! Invalid forge version \\\"$MC_VERSION\\\" !!!\"\r\n    exit\r\nfi\r\n\r\n#Go into main direction\r\ncd \/mnt\/server\r\n\r\n#Adding .jar when not eding by SERVER_JARFILE\r\nif [[ ! $SERVER_JARFILE = *\\.jar ]]; then\r\n  SERVER_JARFILE=\"$SERVER_JARFILE.jar\"\r\nfi\r\n\r\n#Downloading jars\r\necho -e \"Downloading forge version \\\"$MC_VERSION\\\"\"\r\ncurl -o installer.jar -sS https:\/\/files.minecraftforge.net\/maven\/net\/minecraftforge\/forge\/$MC_VERSION\/forge-$MC_VERSION-installer.jar\r\ncurl -o $SERVER_JARFILE -sS https:\/\/files.minecraftforge.net\/maven\/net\/minecraftforge\/forge\/$MC_VERSION\/forge-$MC_VERSION-universal.jar\r\n\r\n#Checking if downloaded jars exist\r\nif [ ! -f .\/installer.jar ] || [ ! -f .\/$SERVER_JARFILE ]; then\r\n    echo \"!!! Error by downloading forge version \\\"$MC_VERSION\\\" !!!\"\r\n    exit\r\nfi\r\n\r\n#Installing server\r\necho -e \"Installing forge server.\\n\"\r\njava -jar installer.jar --installServer\r\n\r\n#Deleting installer.jar\r\necho -e \"Deleting installer.jar file.\\n\"\r\nrm -rf installer.jar",
              "entry": "bash",
              "container": "openjdk:8",
              "extends": null
            },
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00",
            "relationships": {
              "nest": {
                "object": "nest",
                "attributes": {
                  "id": 1,
                  "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
                  "author": "support@pterodactyl.io",
                  "name": "Minecraft",
                  "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
                  "created_at": "2019-12-22T04:42:51+00:00",
                  "updated_at": "2019-12-22T04:42:51+00:00"
                }
              },
              "servers": {
                "object": "list",
                "data": []
              }
            }
          }
        },
        {
          "object": "egg",
          "attributes": {
            "id": 3,
            "uuid": "2ad75dfd-892d-4441-a452-6d7be7cc895a",
            "name": "Paper",
            "nest": 1,
            "author": "parker@pterodactyl.io",
            "description": "High performance Spigot fork that aims to fix gameplay and mechanics inconsistencies.",
            "docker_image": "quay.io\/pterodactyl\/core:java",
            "config": {
              "files": {
                "server.properties": {
                  "parser": "properties",
                  "find": {
                    "server-ip": "0.0.0.0",
                    "server-port": "{{server.build.default.port}}"
                  }
                }
              },
              "startup": {
                "done": ")! For help, type ",
                "userInteraction": [
                  "Go to eula.txt for more info."
                ]
              },
              "stop": "stop",
              "logs": [],
              "extends": null
            },
            "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -Dterminal.jline=false -Dterminal.ansi=true -jar {{SERVER_JARFILE}}",
            "script": {
              "privileged": true,
              "install": "#!\/bin\/ash\r\n# Paper Installation Script\r\n#\r\n# Server Files: \/mnt\/server\r\napk add --no-cache --update curl jq\r\n\r\nif [ -n \"${DL_PATH}\" ]; then\r\n    echo -e \"using supplied download url\"\r\n    DOWNLOAD_URL=`eval echo $(echo ${DL_PATH} | sed -e 's\/{{\/${\/g' -e 's\/}}\/}\/g')`\r\nelse\r\n    VER_EXISTS=`curl -s https:\/\/papermc.io\/api\/v1\/paper | jq -r --arg VERSION $MINECRAFT_VERSION '.versions[] | IN($VERSION)' | grep true`\r\n    LATEST_PAPER_VERSION=`curl -s https:\/\/papermc.io\/api\/v1\/paper | jq -r '.versions' | jq -r '.[0]'`\r\n    \r\n    if [ \"${VER_EXISTS}\" == \"true\" ]; then\r\n        echo -e \"Version is valid. Using version ${MINECRAFT_VERSION}\"\r\n    else\r\n        echo -e \"Using the latest paper version\"\r\n        MINECRAFT_VERSION=${LATEST_PAPER_VERSION}\r\n    fi\r\n    \r\n    BUILD_EXISTS=`curl -s https:\/\/papermc.io\/api\/v1\/paper\/${MINECRAFT_VERSION} | jq -r --arg BUILD ${BUILD_NUMBER} '.builds.all[] | IN($BUILD)' | grep true`\r\n    LATEST_PAPER_BUILD=`curl -s https:\/\/papermc.io\/api\/v1\/paper\/${MINECRAFT_VERSION} | jq -r '.builds.latest'`\r\n    \r\n    if [ \"${BUILD_EXISTS}\" == \"true\" ] || [ ${BUILD_NUMBER} == \"latest\" ]; then\r\n        echo -e \"Build is valid. Using version ${BUILD_NUMBER}\"\r\n    else\r\n        echo -e \"Using the latest paper build\"\r\n        BUILD_NUMBER=${LATEST_PAPER_BUILD}\r\n    fi\r\n    \r\n    echo \"Version being downloaded\"\r\n    echo -e \"MC Version: ${MINECRAFT_VERSION}\"\r\n    echo -e \"Build: ${BUILD_NUMBER}\"\r\n    DOWNLOAD_URL=https:\/\/papermc.io\/api\/v1\/paper\/${MINECRAFT_VERSION}\/${BUILD_NUMBER}\/download \r\nfi\r\n\r\ncd \/mnt\/server\r\n\r\necho -e \"running curl -o ${SERVER_JARFILE} ${DOWNLOAD_URL}\"\r\n\r\nif [ -f ${SERVER_JARFILE} ]; then\r\n    mv ${SERVER_JARFILE} ${SERVER_JARFILE}.old\r\nfi\r\n\r\ncurl -o ${SERVER_JARFILE} ${DOWNLOAD_URL}\r\n\r\nif [ ! -f server.properties ]; then\r\n    echo -e \"Downloading MC server.properties\"\r\n    curl -o server.properties https:\/\/raw.githubusercontent.com\/parkervcp\/eggs\/master\/minecraft_java\/server.properties\r\nfi",
              "entry": "ash",
              "container": "alpine:3.9",
              "extends": null
            },
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00",
            "relationships": {
              "nest": {
                "object": "nest",
                "attributes": {
                  "id": 1,
                  "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
                  "author": "support@pterodactyl.io",
                  "name": "Minecraft",
                  "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
                  "created_at": "2019-12-22T04:42:51+00:00",
                  "updated_at": "2019-12-22T04:42:51+00:00"
                }
              },
              "servers": {
                "object": "list",
                "data": []
              }
            }
          }
        },
        {
          "object": "egg",
          "attributes": {
            "id": 4,
            "uuid": "00274063-5d21-439f-80b9-c4cc0dba8188",
            "name": "Sponge (SpongeVanilla)",
            "nest": 1,
            "author": "support@pterodactyl.io",
            "description": "SpongeVanilla is the SpongeAPI implementation for Vanilla Minecraft.",
            "docker_image": "quay.io\/pterodactyl\/core:java-glibc",
            "config": {
              "files": {
                "server.properties": {
                  "parser": "properties",
                  "find": {
                    "server-ip": "0.0.0.0",
                    "enable-query": "true",
                    "server-port": "{{server.build.default.port}}",
                    "query.port": "{{server.build.default.port}}"
                  }
                }
              },
              "startup": {
                "done": ")! For help, type ",
                "userInteraction": [
                  "Go to eula.txt for more info."
                ]
              },
              "stop": "stop",
              "logs": {
                "custom": false,
                "location": "logs\/latest.log"
              },
              "extends": null
            },
            "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
            "script": {
              "privileged": true,
              "install": "#!\/bin\/ash\n# Sponge Installation Script\n#\n# Server Files: \/mnt\/server\n\napk update\napk add curl\n\ncd \/mnt\/server\n\ncurl -sSL \"https:\/\/repo.spongepowered.org\/maven\/org\/spongepowered\/spongevanilla\/${SPONGE_VERSION}\/spongevanilla-${SPONGE_VERSION}.jar\" -o ${SERVER_JARFILE}",
              "entry": "ash",
              "container": "alpine:3.9",
              "extends": null
            },
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00",
            "relationships": {
              "nest": {
                "object": "nest",
                "attributes": {
                  "id": 1,
                  "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
                  "author": "support@pterodactyl.io",
                  "name": "Minecraft",
                  "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
                  "created_at": "2019-12-22T04:42:51+00:00",
                  "updated_at": "2019-12-22T04:42:51+00:00"
                }
              },
              "servers": {
                "object": "list",
                "data": []
              }
            }
          }
        },
        {
          "object": "egg",
          "attributes": {
            "id": 5,
            "uuid": "cd4cc5cf-de80-4a50-b458-dbd7d3193175",
            "name": "Vanilla Minecraft",
            "nest": 1,
            "author": "support@pterodactyl.io",
            "description": "Minecraft is a game about placing blocks and going on adventures. Explore randomly generated worlds and build amazing things from the simplest of homes to the grandest of castles. Play in Creative Mode with unlimited resources or mine deep in Survival Mode, crafting weapons and armor to fend off dangerous mobs. Do all this alone or with friends.",
            "docker_image": "quay.io\/pterodactyl\/core:java",
            "config": {
              "files": {
                "server.properties": {
                  "parser": "properties",
                  "find": {
                    "server-ip": "0.0.0.0",
                    "enable-query": "true",
                    "server-port": "{{server.build.default.port}}",
                    "query.port": "{{server.build.default.port}}"
                  }
                }
              },
              "startup": {
                "done": ")! For help, type ",
                "userInteraction": [
                  "Go to eula.txt for more info."
                ]
              },
              "stop": "stop",
              "logs": {
                "custom": false,
                "location": "logs\/latest.log"
              },
              "extends": null
            },
            "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
            "script": {
              "privileged": true,
              "install": "#!\/bin\/ash\r\n# Vanilla MC Installation Script\r\n#\r\n# Server Files: \/mnt\/server\r\napk update\r\napk add curl jq\r\n\r\ncd \/mnt\/server\r\n\r\nLATEST_VERSION=`curl https:\/\/launchermeta.mojang.com\/mc\/game\/version_manifest.json | jq -r '.latest.release'`\r\n\r\nif [ -z \"$VANILLA_VERSION\" ] || [ \"$VANILLA_VERSION\" == \"latest\" ]; then\r\n  MANIFEST_URL=$(curl https:\/\/launchermeta.mojang.com\/mc\/game\/version_manifest.json | jq .versions | jq -r '.[] | select(.id == \"'$LATEST_VERSION'\") | .url')\r\nelse\r\n  MANIFEST_URL=$(curl https:\/\/launchermeta.mojang.com\/mc\/game\/version_manifest.json | jq .versions | jq -r '.[] | select(.id == \"'$VANILLA_VERSION'\") | .url')\r\nfi\r\n\r\nDOWNLOAD_URL=`curl $MANIFEST_URL | jq .downloads.server | jq -r '. | .url'`\r\n\r\ncurl -o ${SERVER_JARFILE} $DOWNLOAD_URL",
              "entry": "ash",
              "container": "alpine:3.9",
              "extends": null
            },
            "created_at": "2019-12-22T04:42:51+00:00",
            "updated_at": "2019-12-22T04:42:51+00:00",
            "relationships": {
              "nest": {
                "object": "nest",
                "attributes": {
                  "id": 1,
                  "uuid": "58bde975-ec57-4af2-b241-1426ac6d6d59",
                  "author": "support@pterodactyl.io",
                  "name": "Minecraft",
                  "description": "Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!",
                  "created_at": "2019-12-22T04:42:51+00:00",
                  "updated_at": "2019-12-22T04:42:51+00:00"
                }
              },
              "servers": {
                "object": "list",
                "data": [
                  {
                    "object": "server",
                    "attributes": {
                      "id": 5,
                      "external_id": "RemoteId1",
                      "uuid": "1a7ce997-259b-452e-8b4e-cecc464142ca",
                      "identifier": "1a7ce997",
                      "name": "Wuhu Island",
                      "description": "Matt from Wii Sports",
                      "suspended": false,
                      "limits": {
                        "memory": 512,
                        "swap": 0,
                        "disk": 200,
                        "io": 500,
                        "cpu": 0,
                        "threads": null
                      },
                      "feature_limits": {
                        "databases": 5,
                        "allocations": 5,
                        "backups": 2
                      },
                      "user": 1,
                      "node": 1,
                      "allocation": 1,
                      "nest": 1,
                      "egg": 5,
                      "pack": null,
                      "container": {
                        "startup_command": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
                        "image": "quay.io\/pterodactyl\/core:java",
                        "installed": true,
                        "environment": {
                          "SERVER_JARFILE": "server.jar",
                          "VANILLA_VERSION": "latest",
                          "STARTUP": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
                          "P_SERVER_LOCATION": "Test",
                          "P_SERVER_UUID": "1a7ce997-259b-452e-8b4e-cecc464142ca"
                        }
                      },
                      "updated_at": "2020-06-13T04:20:53+00:00",
                      "created_at": "2019-12-23T06:46:27+00:00"
                    }
                  }
                ]
              }
            }
          }
        }
      ]
    }

### **GET** [ /{egg} ] Egg details

    https://pterodactyl.file.properties/api/application/nests/1/eggs/1

Retrieves the specified egg

## Available include parameters

Parameter | Description
---|---
nest | Information about the nest that owns the egg
servers | List of servers using the egg
config | Config options of the egg
script | Egg install script
variables | List of egg variables

Headers

Accept

application/json

Content-Type

application/json

Authorization

    Bearer apikey

* * *

Example request:

[Copy to clipboard](javascript:;)

    curl "https://pterodactyl.file.properties/api/application/nests/1/eggs/1" \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer apikey' \
      -X GET \
      -b 'pterodactyl_session'='eyJpdiI6InhIVXp5ZE43WlMxUU1NQ1pyNWRFa1E9PSIsInZhbHVlIjoiQTNpcE9JV3FlcmZ6Ym9vS0dBTmxXMGtST2xyTFJvVEM5NWVWbVFJSnV6S1dwcTVGWHBhZzdjMHpkN0RNdDVkQiIsIm1hYyI6IjAxYTI5NDY1OWMzNDJlZWU2OTc3ZDYxYzIyMzlhZTFiYWY1ZjgwMjAwZjY3MDU4ZDYwMzhjOTRmYjMzNDliN2YifQ%3D%3D'

Example response - 200:

    {
      "object": "egg",
      "attributes": {
        "id": 1,
        "uuid": "695648dd-01a3-4ced-b075-d4ec4fb9fbf4",
        "name": "Bungeecord",
        "nest": 1,
        "author": "support@pterodactyl.io",
        "description": "For a long time, Minecraft server owners have had a dream that encompasses a free, easy, and reliable way to connect multiple Minecraft servers together. BungeeCord is the answer to said dream. Whether you are a small server wishing to string multiple game-modes together, or the owner of the ShotBow Network, BungeeCord is the ideal solution for you. With the help of BungeeCord, you will be able to unlock your community's full potential.",
        "docker_image": "quay.io\/pterodactyl\/core:java",
        "config": {
          "files": {
            "config.yml": {
              "parser": "yaml",
              "find": {
                "listeners[0].query_enabled": true,
                "listeners[0].query_port": "{{server.build.default.port}}",
                "listeners[0].host": "0.0.0.0:{{server.build.default.port}}",
                "servers.*.address": {
                  "127.0.0.1": "{{config.docker.interface}}",
                  "localhost": "{{config.docker.interface}}"
                }
              }
            }
          },
          "startup": {
            "done": "Listening on ",
            "userInteraction": [
              "Listening on \/0.0.0.0:25577"
            ]
          },
          "stop": "end",
          "logs": {
            "custom": false,
            "location": "proxy.log.0"
          },
          "extends": null
        },
        "startup": "java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}",
        "script": {
          "privileged": true,
          "install": "#!\/bin\/ash\n# Bungeecord Installation Script\n#\n# Server Files: \/mnt\/server\napk update\napk add curl\n\ncd \/mnt\/server\n\nif [ -z \"${BUNGEE_VERSION}\" ] || [ \"${BUNGEE_VERSION}\" == \"latest\" ]; then\n    BUNGEE_VERSION=\"lastStableBuild\"\nfi\n\ncurl -o ${SERVER_JARFILE} https:\/\/ci.md-5.net\/job\/BungeeCord\/${BUNGEE_VERSION}\/artifact\/bootstrap\/target\/BungeeCord.jar",
          "entry": "ash",
          "container": "alpine:3.9",
          "extends": null
        },
        "created_at": "2019-12-22T04:42:51+00:00",
        "updated_at": "2019-12-22T04:42:51+00:00"
      }
    }