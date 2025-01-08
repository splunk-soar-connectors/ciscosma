[comment]: # "Auto-generated SOAR connector documentation"
# Cisco SMA

Publisher: Splunk  
Connector Version: 1.0.0  
Product Vendor: Cisco  
Product Name: Cisco SMA  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.3.0  

App integration for Cisco SMA, Secure Email and Web Manager

# Splunk> Phantom

Welcome to the open-source repository for Splunk> Phantom's ciscosma App.

Please have a look at our [Contributing Guide](https://github.com/Splunk-SOAR-Apps/.github/blob/main/.github/CONTRIBUTING.md) if you are interested in contributing, raising issues, or learning more about open-source Phantom apps.

## Legal and License

This Phantom App is licensed under the Apache 2.0 license. Please see our [Contributing Guide](https://github.com/Splunk-SOAR-Apps/.github/blob/main/.github/CONTRIBUTING.md#legal-notice) for further details.


### Configuration variables
This table lists the configuration variables required to operate Cisco SMA. These variables are specified when configuring a Cisco SMA asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**host** |  required  | string | Hostname or IP address of Cisco SMA
**username** |  required  | string | Username for host
**password** |  required  | password | Password for host

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[search quarantine messages](#action-search-quarantine-messages) - Search for messages in the spam quarantine  
[search general quarantine messages](#action-search-general-quarantine-messages) - Search for messages in Policy, Virus, Outbreak, and other quarantines  
[get message details](#action-get-message-details) - Retrieve details of a quarantined message  
[release email](#action-release-email) - Release a quarantined email message  
[delete email](#action-delete-email) - Delete a quarantined email message  
[search tracking messages](#action-search-tracking-messages) - Search for messages in message tracking  
[get tracking details](#action-get-tracking-details) - Retrieve detailed tracking information for a message  
[search list](#action-search-list) - Search safelist or blocklist entries  
[add list entry](#action-add-list-entry) - Add an entry to the spam quarantine safelist or blocklist  
[edit list entry](#action-edit-list-entry) - Edit an entry in the spam quarantine safelist or blocklist  
[delete list entry](#action-delete-list-entry) - Delete an entry from the spam quarantine safelist or blocklist  
[get statistics report](#action-get-statistics-report) - Retrieve statistical reports  
[download attachment](#action-download-attachment) - Download attachment from a message  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'search quarantine messages'
Search for messages in the spam quarantine

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start_date** |  required  | Start date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**end_date** |  required  | End date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**order_by** |  optional  | Field to sort results by | string | 
**order_direction** |  optional  | Sort direction | string | 
**offset** |  optional  | Number of records to skip/offset | numeric | 
**limit** |  optional  | Max number of records to return | numeric | 
**envelope_recipient_filter_operator** |  optional  | Operator for envelope recipient filter | string | 
**envelope_recipient_filter_value** |  optional  | Value for envelope recipient filter | string | 
**filter_operator** |  optional  | Operator for general filter | string | 
**filter_value** |  optional  | Value for general filter | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.start_date | string |  |  
action_result.parameter.end_date | string |  |  
action_result.parameter.order_by | string |  |  
action_result.parameter.order_direction | string |  |  
action_result.parameter.offset | numeric |  |  
action_result.parameter.limit | numeric |  |  
action_result.parameter.envelope_recipient_filter_operator | string |  |  
action_result.parameter.envelope_recipient_filter_value | string |  |  
action_result.parameter.filter_operator | string |  |  
action_result.parameter.filter_value | string |  |  
action_result.data.\*.mid | numeric |  `cisco sma message id`  |  
action_result.data.\*.attributes.subject | string |  |  
action_result.data.\*.attributes.date | string |  |  
action_result.data.\*.attributes.fromAddress | string |  `email`  |  
action_result.data.\*.attributes.toAddress | string |  `email`  |  
action_result.data.\*.attributes.envelopeRecipient | string |  `email`  |  
action_result.data.\*.attributes.size | string |  |  
action_result.summary.total_messages | numeric |  |  
action_result.summary.messages_returned | numeric |  |  
action_result.message | string |  |    

## action: 'search general quarantine messages'
Search for messages in Policy, Virus, Outbreak, and other quarantines

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start_date** |  required  | Start date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**end_date** |  required  | End date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**quarantines** |  required  | Comma-separated list of quarantines to search | string | 
**subject_filter_by** |  optional  | How to filter the subject | string | 
**subject_filter_value** |  optional  | Value to filter subject by | string | 
**originating_esa_ip** |  optional  | IP address of the ESA that processed the message | string |  `ip` 
**attachment_name** |  optional  | Filter by attachment name | string | 
**attachment_size_filter_by** |  optional  | How to filter attachment size | string | 
**attachment_size_from** |  optional  | Starting size in KB (for range/more_than) | numeric | 
**attachment_size_to** |  optional  | Ending size in KB (for range/less_than) | numeric | 
**order_by** |  optional  | Field to sort results by | string | 
**order_direction** |  optional  | Sort direction | string | 
**offset** |  optional  | Number of records to skip | numeric | 
**limit** |  optional  | Maximum number of records to return | numeric | 
**envelope_recipient_filter_by** |  optional  | How to filter envelope recipient | string | 
**envelope_recipient_filter_value** |  optional  | Value to filter envelope recipient by | string | 
**envelope_sender_filter_by** |  optional  | How to filter envelope sender | string | 
**envelope_sender_filter_value** |  optional  | Value to filter envelope sender by | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.data.\*.mid | numeric |  `cisco sma message id`  |  
action_result.data.\*.attributes.received | string |  |  
action_result.data.\*.attributes.sender | string |  `email`  |  
action_result.data.\*.attributes.subject | string |  |  
action_result.data.\*.attributes.esaHostName | string |  |  
action_result.data.\*.attributes.inQuarantines | string |  |  
action_result.data.\*.attributes.scheduledExit | string |  |  
action_result.data.\*.attributes.originatingEsaIp | string |  `ip`  |  
action_result.data.\*.attributes.quarantineForReason | string |  |  
action_result.data.\*.attributes.esaMid | numeric |  |  
action_result.data.\*.attributes.recipient | string |  `email`  |  
action_result.data.\*.attributes.size | string |  |  
action_result.summary.total_messages | numeric |  |  
action_result.summary.messages_returned | numeric |  |  
action_result.summary.quarantines | string |  |  
action_result.message | string |  |    

## action: 'get message details'
Retrieve details of a quarantined message

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**message_id** |  required  | Message ID (mid) to retrieve details for | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.message_id | string |  |  
action_result.data.\*.mid | numeric |  `cisco sma message id`  |  
action_result.data.\*.attributes.subject | string |  |  
action_result.data.\*.attributes.date | string |  |  
action_result.data.\*.attributes.fromAddress | string |  `email`  |  
action_result.data.\*.attributes.toAddress | string |  `email`  |  
action_result.data.\*.attributes.envelopeRecipient | string |  `email`  |  
action_result.data.\*.attributes.attachments | string |  `file_name`  |  
action_result.data.\*.attributes.messageBody | string |  |  
action_result.summary.subject | string |  |  
action_result.message | string |  |    

## action: 'release email'
Release a quarantined email message

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**message_id** |  required  | Message ID (mid) to release | string |  `cisco sma message id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.message_id | string |  |  
action_result.data.\*.action | string |  |  
action_result.data.\*.totalCount | numeric |  |  
action_result.summary.total_released | numeric |  |  
action_result.summary.action | string |  |  
action_result.message | string |  |    

## action: 'delete email'
Delete a quarantined email message

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**message_id** |  required  | Message ID (mid) to delete | string |  `cisco sma message id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.message_id | string |  |  
action_result.data.\*.action | string |  |  
action_result.data.\*.totalCount | numeric |  |  
action_result.summary.total_deleted | numeric |  |  
action_result.summary.action | string |  |  
action_result.message | string |  |    

## action: 'search tracking messages'
Search for messages in message tracking

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start_date** |  required  | Start date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**end_date** |  required  | End date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**cisco_host** |  optional  | Specific appliance to search (default: All_Hosts) | string | 
**offset** |  optional  | Number of records to skip/offset | numeric | 
**limit** |  optional  | Max number of records to return | numeric | 
**sender** |  optional  | Filter by sender email address | string | 
**recipient** |  optional  | Filter by recipient email address | string | 
**subject** |  optional  | Filter by message subject | string | 
**message_id** |  optional  | Filter by message ID (mid) | string | 
**status** |  optional  | Filter by message status | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.start_date | string |  |  
action_result.parameter.end_date | string |  |  
action_result.parameter.cisco_host | string |  |  
action_result.parameter.offset | numeric |  |  
action_result.parameter.limit | numeric |  |  
action_result.parameter.sender | string |  |  
action_result.parameter.recipient | string |  |  
action_result.parameter.subject | string |  |  
action_result.parameter.message_id | string |  |  
action_result.parameter.status | string |  |  
action_result.data.\*.attributes.direction | string |  |  
action_result.data.\*.attributes.icid | numeric |  |  
action_result.data.\*.attributes.senderGroup | string |  |  
action_result.data.\*.attributes.sender | string |  `email`  |  
action_result.data.\*.attributes.replyTo | string |  |  
action_result.data.\*.attributes.timestamp | string |  |  
action_result.data.\*.attributes.hostName | string |  |  
action_result.data.\*.attributes.subject | string |  |  
action_result.data.\*.attributes.mid | numeric |  `cisco sma message id`  |  
action_result.data.\*.attributes.isCompleteData | boolean |  |  
action_result.data.\*.attributes.messageStatus | string |  |  
action_result.data.\*.attributes.mailPolicy | string |  |  
action_result.data.\*.attributes.senderIp | string |  `ip`  |  
action_result.data.\*.attributes.verdictChart | string |  |  
action_result.data.\*.attributes.senderDomain | string |  |  
action_result.data.\*.attributes.recipient | string |  `email`  |  
action_result.data.\*.attributes.sbrs | string |  |  
action_result.data.\*.attributes.serialNumber | string |  |  
action_result.summary.total_messages | numeric |  |  
action_result.summary.messages_returned | numeric |  |  
action_result.summary.bad_records | numeric |  |  
action_result.message | string |  |    

## action: 'get tracking details'
Retrieve detailed tracking information for a message

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**mid** |  required  | Message ID (mid) to retrieve details for | string | 
**icid** |  optional  | Incoming Connection ID | string | 
**serial_number** |  optional  | Appliance serial number | string | 
**start_date** |  optional  | Start date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 
**end_date** |  optional  | End date in ISO format (YYYY-MM-DDThh:mm:ss.000Z) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.mid | string |  |  
action_result.parameter.icid | string |  |  
action_result.parameter.serial_number | string |  |  
action_result.parameter.start_date | string |  |  
action_result.parameter.end_date | string |  |  
action_result.data.\*.mid | numeric |  `cisco sma message id`  |  
action_result.data.\*.subject | string |  `email`  |  
action_result.data.\*.messageStatus | string |  |  
action_result.data.\*.direction | string |  |  
action_result.data.\*.sender | string |  `email`  |  
action_result.data.\*.recipient | string |  `email`  |  
action_result.data.\*.attachments | string |  `file_name`  |  
action_result.data.\*.smtpAuthId | string |  |  
action_result.data.\*.midHeader | string |  |  
action_result.data.\*.timestamp | string |  |  
action_result.data.\*.hostName | string |  |  
action_result.data.\*.sendingHostSummary.reverseDnsHostname | string |  |  
action_result.data.\*.sendingHostSummary.ipAddress | string |  `ip`  |  
action_result.data.\*.sendingHostSummary.sbrsScore | string |  |  
action_result.data.\*.summary.\*.timestamp | string |  |  
action_result.data.\*.summary.\*.description | string |  |  
action_result.data.\*.summary.\*.lastEvent | boolean |  |  
action_result.data.\*.messageSize | string |  |  
action_result.data.\*.isCompleteData | boolean |  |  
action_result.data.\*.showDLP | boolean |  |  
action_result.data.\*.showAMP | boolean |  |  
action_result.data.\*.showURL | boolean |  |  
action_result.data.\*.showSummaryTimeBox | boolean |  |  
action_result.data.\*.mailPolicy | string |  |  
action_result.data.\*.senderGroup | string |  |  
action_result.summary.subject | string |  |  
action_result.summary.status | string |  |  
action_result.summary.direction | string |  |  
action_result.message | string |  |    

## action: 'search list'
Search safelist or blocklist entries

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**list_type** |  optional  | Type of list to search | string | 
**view_by** |  optional  | View entries by sender or recipient | string | 
**order_by** |  optional  | Field to sort results by | string | 
**order_direction** |  optional  | Sort direction | string | 
**offset** |  optional  | Number of records to skip/offset | numeric | 
**limit** |  optional  | Max number of records to return | numeric | 
**search** |  optional  | Search term (only supported when order_by=recipient) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.list_type | string |  |  
action_result.parameter.view_by | string |  |  
action_result.parameter.order_by | string |  |  
action_result.parameter.order_direction | string |  |  
action_result.parameter.offset | numeric |  |  
action_result.parameter.limit | numeric |  |  
action_result.parameter.search | string |  |  
action_result.data.\*.senderList | string |  `email`  |  
action_result.data.\*.recipientAddress | string |  `email`  |  
action_result.summary.total_entries | numeric |  |  
action_result.summary.entries_returned | numeric |  |  
action_result.summary.list_type | string |  |  
action_result.message | string |  |    

## action: 'add list entry'
Add an entry to the spam quarantine safelist or blocklist

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**list_type** |  optional  | Type of list to add entry to | string | 
**view_by** |  optional  | Add entry by sender or recipient | string | 
**recipient_addresses** |  optional  | Recipient email addresses (comma-separated if multiple) - Required with view_by=recipient | string | 
**sender_list** |  optional  | Sender addresses or domains (comma-separated if multiple) - Required with view_by=recipient | string | 
**sender_addresses** |  optional  | Sender addresses or domains (comma-separated if multiple) - Required with view_by=sender | string | 
**recipient_list** |  optional  | Recipient email addresses (comma-separated if multiple) - Required with view_by=sender | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.list_type | string |  |  
action_result.parameter.view_by | string |  |  
action_result.parameter.recipient_addresses | string |  |  
action_result.parameter.sender_list | string |  |  
action_result.parameter.sender_addresses | string |  |  
action_result.parameter.recipient_list | string |  |  
action_result.data.\*.action | string |  |  
action_result.data.\*.recipientAddresses | string |  |  
action_result.data.\*.senderList | string |  |  
action_result.data.\*.senderAddresses | string |  |  
action_result.data.\*.recipientList | string |  |  
action_result.summary.list_type | string |  |  
action_result.summary.view_by | string |  |  
action_result.summary.status | string |  |  
action_result.message | string |  |    

## action: 'edit list entry'
Edit an entry in the spam quarantine safelist or blocklist

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**list_type** |  optional  | Type of list to edit entry in | string | 
**view_by** |  optional  | Edit entry by sender or recipient | string | 
**recipient_addresses** |  optional  | Recipient email addresses (comma-separated if multiple) - Required with view_by=recipient | string | 
**sender_list** |  optional  | Sender addresses or domains (comma-separated if multiple) - Required with view_by=recipient | string | 
**sender_addresses** |  optional  | Sender addresses or domains (comma-separated if multiple) - Required with view_by=sender | string | 
**recipient_list** |  optional  | Recipient email addresses (comma-separated if multiple) - Required with view_by=sender | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.list_type | string |  |  
action_result.parameter.view_by | string |  |  
action_result.parameter.recipient_addresses | string |  |  
action_result.parameter.sender_list | string |  |  
action_result.parameter.sender_addresses | string |  |  
action_result.parameter.recipient_list | string |  |  
action_result.data.\*.action | string |  |  
action_result.data.\*.recipientAddresses | string |  |  
action_result.data.\*.senderList | string |  |  
action_result.data.\*.senderAddresses | string |  |  
action_result.data.\*.recipientList | string |  |  
action_result.summary.list_type | string |  |  
action_result.summary.view_by | string |  |  
action_result.summary.status | string |  |  
action_result.message | string |  |    

## action: 'delete list entry'
Delete an entry from the spam quarantine safelist or blocklist

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**list_type** |  optional  | Type of list to delete entry from | string | 
**view_by** |  optional  | Delete entry by sender or recipient | string | 
**recipient_list** |  optional  | Recipient email addresses (comma-separated if multiple) - Required with view_by=recipient | string | 
**sender_list** |  optional  | Sender addresses or domains (comma-separated if multiple) - Required with view_by=sender | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.list_type | string |  |  
action_result.parameter.view_by | string |  |  
action_result.parameter.recipient_list | string |  |  
action_result.parameter.sender_list | string |  |  
action_result.data.\*.action | string |  |  
action_result.data.\*.totalCount | numeric |  |  
action_result.data.\*.recipientList | string |  |  
action_result.data.\*.senderList | string |  |  
action_result.summary.list_type | string |  |  
action_result.summary.view_by | string |  |  
action_result.summary.total_deleted | numeric |  |  
action_result.summary.status | string |  |  
action_result.message | string |  |    

## action: 'get statistics report'
Retrieve statistical reports

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start_date** |  required  | Start date and time (format: YYYY-MM-DDThh:mm:00.000Z) | string | 
**end_date** |  required  | End date and time (format: YYYY-MM-DDThh:mm:00.000Z) | string | 
**report_type** |  required  | Type of report to retrieve | string | 
**query_type** |  optional  | Type of query | string | 
**order_by** |  optional  | Field to sort results by | string | 
**order_direction** |  optional  | Sort direction | string | 
**offset** |  optional  | Number of records to skip/offset | numeric | 
**limit** |  optional  | Max number of records to return | numeric | 
**top** |  optional  | Number of top records to return | numeric | 
**filter_value** |  optional  | Value to filter by | string | 
**filter_by** |  optional  | Field to filter by | string | 
**filter_operator** |  optional  | Filter operator | string | 
**device_group_name** |  optional  | Name of device group | string | 
**device_name** |  optional  | Name of device | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.parameter.start_date | string |  |  
action_result.parameter.end_date | string |  |  
action_result.parameter.report_type | string |  |  
action_result.parameter.query_type | string |  |  
action_result.parameter.order_by | string |  |  
action_result.parameter.order_direction | string |  |  
action_result.parameter.offset | numeric |  |  
action_result.parameter.limit | numeric |  |  
action_result.parameter.top | numeric |  |  
action_result.parameter.filter_value | string |  |  
action_result.parameter.filter_by | string |  |  
action_result.parameter.filter_operator | string |  |  
action_result.parameter.device_group_name | string |  |  
action_result.parameter.device_name | string |  |  
action_result.data.\*.type | string |  |  
action_result.data.\*.resultSet | string |  |  
action_result.summary.report_type | string |  |  
action_result.summary.total_count | numeric |  |  
action_result.message | string |  |    

## action: 'download attachment'
Download attachment from a message

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**message_id** |  required  | Message ID (mid) of message | string |  `cisco sma message id` 
**attachment_id** |  required  | ID of attachment to download | string | 
**quarantine_type** |  required  | Type of quarantine | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |  
action_result.data.\*.vault_id | string |  |  
action_result.data.\*.filename | string |  |  
action_result.summary.vault_id | string |  |  
action_result.summary.filename | string |  |  
action_result.summary.size | string |  |  
action_result.message | string |  |  