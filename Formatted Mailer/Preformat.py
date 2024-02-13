
formats = {
    "Promotional":"Announce special promotions, discounts, or sales events.\nEncourage customers to take advantage of limited-time offers."
    ,"Product Launch":"Introduce and promote new products or services to your audience.\nHighlight key features and benefits to generate interest."
    ,"Newsletter":"Provide regular updates, news, or insights about your company.\nShare industry trends, tips, or educational content with subscribers."
    ,"Welcome":"Greet new subscribers or customers when they join your mailing list.\nProvide a warm welcome, introduce your brand, and set expectations."
    ,"Abandoned Cart":"Remind customers about items left in their shopping cart.\nOffer incentives or discounts to encourage them to complete their purchase."
    ,"Event Invitations":"Invite subscribers to attend webinars, conferences, or other events.\nProvide event details and encourage registration."
    ,"Survey and Feedback":"Request feedback from customers about their experiences.\nUse surveys to gather insights, improve products/services, and enhance customer satisfaction."
    ,"Transactional":"Confirm orders, shipping details, or subscription renewals.\nProvide receipts, order confirmations, and account updates."
    ,"Announcement":"Share important company news, such as new partnerships, acquisitions, or achievements.\nKeep your audience informed about significant developments."
    ,"Educational":"Offer educational content, tutorials, or how-to guides related to your products or industry.\nEstablish your brand as an authority and provide value to your audience."
    ,"Birthday or Anniversary":"Send personalized messages, offers, or discounts to celebrate customers' birthdays or anniversaries with your brand."
    ,"Re-engagement":"Target inactive subscribers and encourage them to re-engage with your content or products.\nOffer special incentives to bring them back into the fold."
    ,"Cross-Sell and Up-Sell":"Recommend complementary products or upgrades based on customers' previous purchases.\nEncourage additional spending or product upgrades."
    ,"Holiday or Seasonal":"Capitalize on holidays or seasonal events to promote special offers or themed campaigns.\nAlign your messaging with the holiday spirit or specific occasions."
}


def show_format():
    for k,v in formats.items():
        print("-->  ",k)
        print(v)
        print()

if __name__ == "__main__":
    show_format()
    