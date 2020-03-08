# def start_task_queues():
#     # Starting TaskQueues
#     _app_logger.info("Starting TaskQueues...")
#     for queue in TaskQueue.QUEUES:
#         queue.start()

# def activate_scheduler():
#     _app_logger.info("Activating Scheduler...")
#     from .scheduling.scheduler import Scheduler, register_for_schedule_change
#     from .workers.worker_deployment import WorkerDeployment
#     WorkerDeployment.DRY_RUN = app.config['SCHEDULER_DRY_RUN']
#     if WorkerDeployment.DRY_RUN:
#         _app_logger.warning("***** Scheduler is in DRY RUN mode, no requests will be made to Kubernetes. *****")
#     else:
#         _app_logger.warning("***** Scheduler is in PRODUCTION MODE mode, Kubernetes calls will be performed. *****")
#     Scheduler.execute_and_reschedule()
#     register_for_schedule_change(app)


#  if app.config['TASK_QUEUES_AUTOSTART']:
#     start_task_queues()
# else:
#     app.before_first_request(start_task_queues)


# # -------------------------------------------------------------------------------
# # application startup
# # -------------------------------------------------------------------------------

# if app.config['TASK_QUEUES_AUTOSTART']:
#     start_task_queues()
# else:
#     app.before_first_request(start_task_queues)


# if app.config['SCHEDULER_AUTOSTART']:
#     if app.config['TASK_QUEUES_AUTOSTART']:
#         activate_scheduler()
#     else:
#         app.before_first_request(activate_scheduler)
