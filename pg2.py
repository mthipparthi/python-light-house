# # pdf_merging.py

# from PyPDF2 import PdfFileReader, PdfFileWriter


# def merge_pdfs(paths, output):
#     pdf_writer = PdfFileWriter()

#     for path in paths:
#         pdf_reader = PdfFileReader(path)
#         for page in range(pdf_reader.getNumPages()):
#             # Add each page to the writer object
#             pdf_writer.addPage(pdf_reader.getPage(page))

#     # Write out the merged PDF
#     with open(output, "wb") as out:
#         pdf_writer.write(out)


# if __name__ == "__main__":
#     paths = [
#         "/Users/mahesh.thipparthi/Downloads/dl-1.pdf",
#         "/Users/mahesh.thipparthi/Downloads/dl-2.pdf",
#     ]
#     merge_pdfs(paths, output="merged.pdf")


# from abc import abstractmethod


# class Base:
#     def __init__(self):
#         pass

#     @abstractmethod
#     def dispatch(self):
#         raise NotImplementedError

#     def execute(self):
#         self.dispatch()


# def main():
#     b = Base()
#     b.execute()


# class GroupStatisticsDispatchTask(StatisticsDispatchTask):
#     def __init__(self, stat_event_list):
#         BaseBackgroundTask.__init__(self)
#         self.stat_event_list = stat_event_list
#         self._max_retries =  c.C_STATISTICS_SERVICE_V2_MAX_RETRY

#     def dispatch_group_stats(self):
#         pass

#     def dispatch_segments(self):
#         pass

#     def dispatch(self, payload):
#         num_try = 0
#         endpoint = '{}stats/event'.format(
#         flask.current_app.config[c.C_URL_STATISTICS_SERVICE_V2_INTERNAL])
#         while num_try < self._max_retries:
#             num_try = num_try + 1
#             headers = {
#                     H_X_API_KEY:
#                 flask.current_app.config[c.C_STATISTICS_SERVICE_V2_API_KEY]}

#             response = request_executor.request_put(
#                     endpoint, headers=headers,
#                     data=payload, timeout=(CONNECT_TIMEOUT, 6.20),
#                     do_not_retry_on_read_timeout=True)

#             if response.status_code:
#                     last_response_code = response.status_code

#                 # need a better way to tell when it fails - even malformed data
#                 # returns 200
#             if response.ok:
#                     success = True
#                     break
#             elif response.status_code >= 500:
#                     msg = ("[Stat v2] stat api gate error  due to status: {}. "
#                            "Will retry event - number of try: {}").format(
#                                response.status_code, num_try)
#                     nr.newrelic_record_custom_event(
#                         nr.EventType.EXPECTED_ERROR,
#                         {'message': msg},
#                         remote_response=response
#                     )
#                     continue   # retry for 5xx status
#             else:
#                 msg = ("[Stat v2] stat api gate error due to status: "
#                            "{}").format(response.status_code)
#                 nr.newrelic_record_custom_event(
#                         nr.EventType.EXPECTED_ERROR,
#                         {'message': msg},
#                         remote_response=response
#                     )
#                 break

#         if success is False:
#             msg = ("[Stat v2] Sending stat event failed due to status: "
#                        "{}. Event {}/{}").format(
#                            last_response_code,
#                            idx+1,
#                            len(self.stat_event_list))
#             nr.newrelic_record_custom_event(
#                     nr.EventType.EXPECTED_ERROR,
#                     {'message': msg}
#                 )


import requests
import functools


def retry(max_tries=3):
    def _decorator(method):
        @functools.wraps(method)
        def _wrapper(*args, **kwargs):
            num_try = 0
            rv = True
            while num_try < max_tries:
                num_try = num_try + 1
                response = method(*args, **kwargs)
                if response.ok:
                    break
                elif response.status_code >= 500:
                    continue
                else:
                    break
            return rv

        return _wrapper

    return _decorator


@retry()
def get_bin():
    response = requests.get("http://httpbin.org/status/500",)
    print(response)
    return response


def main():
    get_bin()


if __name__ == "__main__":
    main()

